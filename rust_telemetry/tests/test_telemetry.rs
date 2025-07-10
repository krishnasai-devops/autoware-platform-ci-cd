use rust_telemetry::generate_message;

#[test]
fn test_message_format() {
    let msg = generate_message("engine");
    assert!(msg.contains("engine"));
}