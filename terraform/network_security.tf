variable "security_group_id" {
  description = "El ID del grupo de seguridad donde bloquear IPs"
  type        = string
  default     = "sg-05042cc483ca3d3b3"
}

locals {
 
  raw_ips      = fileexists("${path.module}/../data/blacklist.txt") ? split("\n", trimspace(file("${path.module}/../data/blacklist.txt"))) : []
  ips_to_block = [for ip in local.raw_ips : ip if ip != ""]
}

resource "aws_security_group_rule" "block_attacker" {
  for_each          = toset(local.ips_to_block)

  type              = "ingress"
  from_port         = 0
  to_port           = 0
  protocol          = "-1" 
  cidr_blocks       = ["${each.value}/32"]
  security_group_id = var.security_group_id
  description       = "Blocked by SecOps-Agent: Intrusion detection"
}
