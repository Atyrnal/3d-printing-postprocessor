#![cfg_attr(target_os = "windows", windows_subsystem = "windows")]

use std::collections::HashMap;
use std::env;
use std::fs::{File};
use std::io::{BufRead, BufReader};
use std::rc::Rc;
use std::cell::RefCell;
use chrono::Local;
use slint::Weak;
use uuid::Uuid;
use regex::Regex;

//const emailRegex = "[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*@(?:[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?\.)+[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?"


slint::include_modules!();

const TARGETED_PROPERTIES : [&str; 7] = ["total filament used [g]", "filament_type", "printer_settings_id", "estimated printing time (normal mode)", "filament_settings_id", "print_settings_id", "job_name"];

#[allow(non_snake_case)]
#[derive(Debug)]
#[allow(dead_code)] //Remove this eventually
struct Print {
    HumanName : String,
    Email : String,
    PrinterName : String,
    FileName : String,
    FilamentType : String,
    FilamentOwner : String,
    FilamentWeight : String,
    Time : String,
    UUID : String,
    Timestamp : i64
}

struct PrintInfo {
    printer_settings : String,
    filament_settings : String,
    print_settings : String,
    filename : String,
    filament_weight : String,
    print_time : String,
}

fn main() {
    //Get args / gcode file path from OrcaSlicer
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: post_processor <gcode filepath>");
        std::process::exit(1);
    }

    let staff_pins : Vec<String> = vec!["1234".to_string()];

    let gcode_path = &args[1];
    println!("Processing gcode file: {}", gcode_path);
    let mut gcode_properties: HashMap<String, String> = HashMap::new();

    if let Ok(file) = File::open(gcode_path) { //Open specified GCode file
        let reader = BufReader::new(file); //Read the file
        for line in reader.lines() {
            let line = line.unwrap();

            for p in TARGETED_PROPERTIES.iter() {
                if line.starts_with(&format!("; {} = ", p)) { //Check each line for properties we care about
                    let value = line.clone().split("=").last().unwrap_or("").trim().to_string(); //Rust is a weird f*cking language
                    gcode_properties.insert(p.to_string(), value); //Add the property to the hashmap
                }
            }
        }
    }

    #[allow(unused_variables)] //Remove eventually
    let print: Print;

    let gui_info : PrintInfo = PrintInfo { 
        printer_settings: gcode_properties[TARGETED_PROPERTIES[2]].clone(), 
        filament_settings: gcode_properties[TARGETED_PROPERTIES[4]].clone(), 
        print_settings: gcode_properties[TARGETED_PROPERTIES[5]].clone(), 
        filename: {
            /*let filepath: String = gcode_path.clone();
            let fp_split = filepath.split("/").last().unwrap_or("").trim().split(".");
            fp_split.clone().take(fp_split.count()-1).collect::<Vec<&str>>().join(".").trim().to_string()*/
            gcode_properties[TARGETED_PROPERTIES[6]].clone() //Get from modified G-Code via preset including {input_filename_base}
        }, 
        filament_weight: format!("{}g",gcode_properties[TARGETED_PROPERTIES[0]].clone()), 
        print_time: gcode_properties[TARGETED_PROPERTIES[3]].clone()
    };

    match gui(gui_info, staff_pins) {
        Ok((human_name, email, filament_owner, staff_pin )) => {
            print = Print {
                HumanName : human_name.trim().to_string(),
                Email : email.trim().to_string(),
                PrinterName : {
                    let full_string : String = gcode_properties[TARGETED_PROPERTIES[2]].clone();

                    let printer_type: String = full_string.split("(").nth(0).unwrap_or("").trim().to_string();
                    let printer_number: String = full_string.split("#").nth(1).unwrap_or("").split(" ").nth(0).unwrap().trim().to_string();
                    let printer_name: String = full_string.split("#").nth(1).unwrap_or("").split_whitespace().skip(1).collect::<Vec<&str>>().join(" ").trim().to_string();

                    let output : String = format!("{} #{} - {}", printer_type, printer_number, printer_name);
                    let printer_regex = Regex::new(r"^[A-Za-z0-9 ]+\s+#[0-9]+\s+-[A-Za-z0-9 ]+$").unwrap();
                    if printer_regex.is_match(&output) { output } else { full_string }
                },
                FileName : {
                    /*let filepath: String = gcode_path.clone();
                    let fp_split = filepath.split("/").last().unwrap_or("").trim().split(".");
                    fp_split.clone().take(fp_split.count()-1).collect::<Vec<&str>>().join(".").trim().to_string()*/
                    gcode_properties[TARGETED_PROPERTIES[6]].clone()
                },
                FilamentType : gcode_properties[TARGETED_PROPERTIES[1]].clone(),
                FilamentOwner : if filament_owner == "Personal" { "Personal".to_string() } else { "Makerspace".to_string() },
                FilamentWeight : format!("{}g", gcode_properties[TARGETED_PROPERTIES[0]]),
                Time : Local::now().format("%b %e, %Y, %I:%M:%S %p").to_string(),
                UUID : Uuid::new_v4().to_string(),
                Timestamp : Local::now().timestamp()
            };
            println!("Dialog Submitted")
        }
        Err(e) => {
            eprintln!("GUI error: {}", e);
            std::process::exit(1);
        }
    }

    println!("{:#?}", print);

    //std::io::stdin().read_line(&mut String::new()).unwrap();

}

fn gui(info : PrintInfo, pins : Vec<String>) -> Result<(String, String, String, String), slint::PlatformError> {
    let app = AppWindow::new().unwrap();

    let name_regex : Regex = Regex::new(r"^[A-Za-z\. ]+$").unwrap();
    let email_regex : Regex = Regex::new(r"^[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*@umass\.edu$").unwrap();
    
    let result : Rc<RefCell<Option<(String, String, String, String)>>> = Rc::new(RefCell::new(None)); 

    //Pass print info to GUI
    app.set_printer_settings(slint::SharedString::from(info.printer_settings));
    app.set_print_settings(slint::SharedString::from(info.print_settings));
    app.set_filament_settings(slint::SharedString::from(info.filament_settings));
    app.set_filament_weight(slint::SharedString::from(info.filament_weight));
    app.set_print_time(slint::SharedString::from(info.print_time));
    app.set_filename(slint::SharedString::from(info.filename));


    app.on_sumbit({
        let app_weak: Weak<AppWindow> = app.as_weak();
        let result_clone: Rc<RefCell<Option<(String, String, String, String)>>> = result.clone();
        move |human_name : slint::SharedString, email : slint::SharedString, filament_owner : slint::SharedString, staff_pin : slint::SharedString| {
            let app: AppWindow = app_weak.unwrap();

            let mut errors: bool = false;

            if !name_regex.is_match(&human_name.to_string()) {
                errors = true;
                //Handle invalid name error
                app.set_name_invalid(true);
            } else {
                app.set_name_invalid(false);
            }
            if !email_regex.is_match(&email.to_string()) {
                errors = true;
                //Handle invalid email error
                app.set_email_invalid(true);
            } else {
                app.set_email_invalid(false);
            }
            if &filament_owner.to_string() != "Makerspace" && &filament_owner.to_string() != "Personal" {
                //Shoudl be impossible??
                //Leave handling to main() 
            }
            if !pins.contains(&staff_pin.to_string()) {
                errors = true;
                app.set_pin_invalid(true);
            } else {
                app.set_pin_invalid(false);
            }
            
            if !errors {
                *result_clone.borrow_mut() = Some((
                    human_name.to_string(), 
                    email.to_string(), 
                    filament_owner.to_string(),
                    staff_pin.to_string()
                ));
                let _ = app.hide();
            }
        }
    });

    app.run()?;

    match result.borrow().as_ref() {
        Some(data) => Ok(data.clone()),
        None => {
            Err(slint::PlatformError::Other("No data submitted".into()))
        }
    }
}

//Label information:
//Human Name (get from UI input) (or load from email?)
//Umass Email (get from UI input)
//PrinterName (get from GCode?)
//FileName (given by OrcaSlicer as argument to post_processor)
//FilamentType (get from GCode)
//FilamentOwner (get from UI input)
//FilamentWeight (get from GCode)
//Time (generated)
//UUID (generated)
//Timestamp (generated)
