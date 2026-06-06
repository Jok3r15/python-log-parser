terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "log-parser-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name = "log-parser-vpc"
  }
}

resource "aws_subnet" "private_subnet" {
  vpc_id            = aws_vpc.log-parser-vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "log-parser-vpc-private-subnet"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.log-parser-vpc.id

  tags = {
    Name = "log-parser-vpc-internet-gateway"
  }
}

resource "aws_route_table" "route_table_log_parser" {
  vpc_id = aws_vpc.log-parser-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
}

resource "aws_route_table_association" "route_table_association_log_parser" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.route_table_log_parser.id
}

resource "aws_security_group" "log_parser_sg" {
  name   = "log-parser-sg"
  vpc_id = aws_vpc.log-parser-vpc.id


  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["159.26.98.238/32"]
  }


  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "log_parser_server" {
  ami           = "ami-091138d0f0d41ff90"
  instance_type = "t3.micro"
  key_name      = "log-parser-key"

  subnet_id                   = aws_subnet.private_subnet.id
  vpc_security_group_ids      = [aws_security_group.log_parser_sg.id]
  associate_public_ip_address = true


  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y python3-pip python3-venv git
              cd /home/ubuntu
              git clone https://github.com/Jok3r15/python-log-parser
              cd python-log-parser
              python3 -m venv .venv
              source .venv/bin/activate
              pip install pandas boto3
              # Opcional: podrías poner a correr el script aquí mismo
              # nohup python3 src/parser/main.py &
              EOF

  tags = {
    Name = "log-parser-instance"
  }
}
