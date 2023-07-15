resource "aws_key_pair" "aws-key" {
  key_name   = "makey"
  public_key = file(var.PUBLIC_KEY_PATH) // Path is in the variables file
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = var.ebs-id
  instance_id = aws_instance.grafana.id
}

resource "aws_instance" "docker" {
  ami                    = var.instance_ami
  instance_type          = var.instance_type
  tags                   = var.instance_tags
  vpc_security_group_ids = [aws_security_group.mysecgroup.id]
  subnet_id              = aws_subnet.prod-subnet-public-1.id
  key_name               = aws_key_pair.aws-key.id

  #Clonar o repositório
  provisioner "remote-exec" {
    inline = [
      "git clone https://github.com/strovertz/ufsm-horarios.git",
    ]
  }

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("${var.PRIVATE_KEY_PATH}")
  }

}



