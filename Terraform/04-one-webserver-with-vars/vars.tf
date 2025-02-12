# Input variable: server port
variable "server_port" {
  description = "The port the server will use for HTTP requests"
  default     = "8080"
}

variable "ssh_port" {
  description = "The port the server will use for ssh "
  default     = "22"
}

variable "tags" {
  default = {
    Name = "terraform-example"
  }
}