output "instance_public_ip" {
  description = "La IP pública de mi centinela"
  value       = aws_instance.log_parser_server.public_ip
}
