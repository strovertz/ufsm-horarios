resource "aws_key_pair" "aws-key" {
  key_name   = "makey"
  public_key = file(var.PUBLIC_KEY_PATH) // Path is in the variables file
}

resource "aws_volume_attachment" "ebs_att" {
  device_name = "/dev/sdh"
  volume_id   = var.ebs-id
  instance_id = aws_instance.grafana.id
}

resource "aws_instance" "grafana" {
  ami                    = var.instance_ami
  instance_type          = var.instance_type
  tags                   = var.instance_tags
  vpc_security_group_ids = [aws_security_group.mysecgroup.id]
  subnet_id              = aws_subnet.prod-subnet-public-1.id
  key_name               = aws_key_pair.aws-key.id

  #Jogar o script pra instancia
  provisioner "file" {
    source      = "../automations/separate_rows.py"
    destination = "/tmp/separate_rows.py"
  }
  provisioner "file" {
    source      = "../automations/mysql-grafana.py"
    destination = "/tmp/mysql-grafana.py"
  }
  provisioner "file" {
    source      = "../original_datasets/credits.csv"
    destination = "/tmp/credits.csv"
  }
  provisioner "file" {
    source      = "../original_datasets/titles.csv"
    destination = "/tmp/titles.csv"
  }
  provisioner "file" {
    source      = "./internal-scripts/userdata.sh"
    destination = "/tmp/userdata.sh"
  }
  provisioner "file" {
    source      = "../automations/insert_data.py"
    destination = "/tmp/insert_data.py"
  }
  #Rodar o  script
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/userdata.sh",
      "sudo /tmp/userdata.sh"
    ]
  }
    provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/separate_rows.py",
      "sudo python3 /tmp/separate_rows.py"
    ]
  }
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/insert_data.py",
      "sudo python3 /tmp/insert_data.py"
    ]
  }
   provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/mysql-grafana.py",
      "sudo python3 /tmp/mysql-grafana.py"
    ]
  }

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("${var.PRIVATE_KEY_PATH}")
  }

}



