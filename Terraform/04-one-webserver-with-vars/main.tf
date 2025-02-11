# Configure the AWS provider
provider "aws" {
  region = "us-east-1"
}

# Create a Security Group for an EC2 instance 
resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a Security Group for an EC2 instance
resource "aws_security_group" "ssh" {
  name = "ssh-instance"

  ingress {
    description = "this is the ssh rule"
    from_port   = var.ssh_port
    to_port     = var.ssh_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a Security Group for an EC2 instance
resource "aws_security_group" "icmp" {
  name = "icmp-instance"

  ingress {
    description = "this is the ICMP rule"
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_key_pair" "ssh-key" {
  key_name   = "ssh-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDDuc8TiY2qlWWOZbhmzW5qSDUaXAQoq4Z4udSadNb6/dkLV/nRgVUSEz8fU3dUpK+K5/MaFA2ueTv9nMggKc865UwQhT/VtHW+Inqn2Y9XW6ATwsRfbkC2Knzh0rEhaq9Dw/rWT4ig9dL+/ex+VbK1f19+irWNbXVJSBj0Yk+6dEYF2DbgztNbjWTVnWjpfqH2n/fg6NPHRSbf+CztGYZpOmMj28AxzGm6jdoR6/Pybx/SI8fgzhnVZe57PqFlohhjoVWY6rj6YL/xNorUIi1lxK4OO7qQYBvr9N64zNvnLUjFiWhtRk1wUxhOIj9SwJnrinA58ZdvUa6X5SmWxxizNOAohK351+7z5UZqnLD1A5ZflSaJy2K/iN1J6D2jGlStf5pA17CZyN8TNNfCh6qOsW9Zs7wsQwUILHh9x7c7FsEP+t7lZhm/t2SHFP2tpMld4FR7jNFJUBLA8dnlrXJJMaxwsy5kUDRpBjqOUA/06nVE+x/jXWHo08f/OJth3jeAYEJdc6+Zk+j/+1bWqKOizm343zNL5Bxqn/62N/02usJsMjYolQhF9IE2LxaC12h6xX73ASkqKukihVi9+y9Ev0hUuuyNlo1jdkg49QsOWO6TlfiCM/5PRPmcSsMLXKz+lqezqjhLH3/782XRMc5NFSBnUJs+KLATuSY1u2mShQ== yidgar@gmail.com"
}


# Create an EC2 instance
resource "aws_instance" "example" {
  #ami           = "ami-01816d07b1128cd2d"
  ami           = "ami-05576a079321f21f8"
  instance_type = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.instance.id}",
    "${aws_security_group.ssh.id}",
  "${aws_security_group.icmp.id}"]
  associate_public_ip_address = true

  key_name = "ssh-key"
  tags     = var.tags

  user_data = <<-EOF
	      #!/bin/bash
	      echo "Hello, World" > /home/ec2-user/index.html
	      nohup python3 -m http.server 8080 &
	      EOF
  #nohup busybox httpd -f -p "${var.server_port}" &

  # tags {
  #   Name = "terraform-example"
  # }
}
