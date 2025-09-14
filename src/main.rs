use std::collections::HashMap;
use std::env;
use std::fs::{self, File};
use std::io::{self, BufRead, BufReader};

const TARGETED_PROPERTIES : [&str; 6] = ["total filament used [g]", "filament_type", "printer_model", "printer_settings_id", "printer_notes", "estimated printing time (normal mode)"];

fn main() {
    //Get args / gcode file path from OrcaSlicer
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: post_processor <gcode filename>");
        std::process::exit(1);
    }

    let gcode_path = &args[1];
    println!("Processing gcode file: {}", gcode_path);
    let mut gcode_properties: HashMap<String, String> = HashMap::new();

    if let Ok(file) = File::open(gcode_path) { //Open specified GCode file
        let reader = BufReader::new(file); //Read the file
        for line in reader.lines() {
            let line = line.unwrap();

            for p in TARGETED_PROPERTIES.iter() {
                if line.contains(&format!("{} = ", p)) { //Check each line for properties we care about
                    let value = line.clone().split("=").nth(1).unwrap().trim().to_string(); //Rust is a weird f*cking language
                    gcode_properties.insert(p.to_string(), value); //Add the property to the hashmap
                }
            }
        }
    }

    println!("{:#?}", gcode_properties);
    std::io::stdin().read_line(&mut String::new()).unwrap();

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
