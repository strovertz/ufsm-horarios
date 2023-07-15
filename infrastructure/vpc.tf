resource "aws_vpc" "grafanasql-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  instance_tenancy     = "default"
}

resource "aws_internet_gateway" "prod-igw" {
  vpc_id = aws_vpc.grafanasql-vpc.id
}

resource "aws_security_group" "mysecgroup" {

  name   = "ec2-sec-ports"
  vpc_id = aws_vpc.grafanasql-vpc.id
  
  ingress {
    from_port   = 80 # Porta padrão do HTTP
    to_port     = 80 # Porta padrão do HTTP
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Permite acesso externo
  }

  ingress {
    from_port   = 3000 # Porta padrão do Grafana
    to_port     = 3000 # Porta padrão do Grafana
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Exemplo de dois intervalos de rede permitidos
  }

  ingress {
    from_port   = 3306 # Porta padrão do MySQL
    to_port     = 3306 # Porta padrão do MySQL
    protocol    = "tcp"
    cidr_blocks = ["10.1.0.0/16"] # Exemplo de um intervalo de rede permitido
  }

  # Liberar a porta 80 para acesso livre via Internet
  ingress {
    from_port        = var.aws_secgrp_port
    to_port          = var.aws_secgrp_port
    protocol         = var.tcp
    cidr_blocks      = [var.cidr_blocks]
    ipv6_cidr_blocks = ["::/0"]
  }

  #ssh ingress 
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = var.tcp
    cidr_blocks = [var.cidr_blocks_ssh]
  }
  # Liberar todo o tráfego de saida
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = -1
    cidr_blocks = [var.cidr_blocks]
  }
}

resource "aws_route_table" "prod-public-crt" {
  vpc_id = aws_vpc.grafanasql-vpc.id
  route {
    cidr_block = "0.0.0.0/0"                      // A subnet associada pode alcançar qq um
    gateway_id = aws_internet_gateway.prod-igw.id //CTR utiliza esse ift para alcançar a interner
  }
  tags = {
    Name = "prod-public-crt"
  }
}

resource "aws_route_table_association" "prod-crta-public-subnet-1" {
  subnet_id      = aws_subnet.prod-subnet-public-1.id
  route_table_id = aws_route_table.prod-public-crt.id
} #cria uma conexão entre a subnet e a route table

resource "aws_subnet" "prod-subnet-public-1" {
  vpc_id                  = aws_vpc.grafanasql-vpc.id // Referencing the id of the VPC from abouve code block
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = "true" // Makes this a public subnet
  availability_zone       = "us-east-1a"
}

resource "aws_eip" "grafana_eip" {
  instance = aws_instance.grafana.id
  vpc      = true
}

resource "aws_security_group" "internal" {
  name        = var.grafana-sg
  description = "Security Group for Grafana internal access"

  vpc_id = var.vpc_default
}
