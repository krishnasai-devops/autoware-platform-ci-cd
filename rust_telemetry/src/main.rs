fn main() {
    println!("{}", generate_message("engine"));
}

pub fn generate_message(component: &str) -> String {
    format!("Telemetry from {}", component)
}