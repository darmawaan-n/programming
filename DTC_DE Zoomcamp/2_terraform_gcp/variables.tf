variable "credentials" {
  description = "My Credentials"
  default     = "./keys/credentials.json"
  # default = "~/.config/gcloud/application_default_credentials.json"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "example_dataset"
}

variable "gcs_bucket_name" {
  description = "My GCS Bucket Name"
  default     = "acoustic-portal-411603-terra-bucket"
}

variable "location" {
  description = "My Project Location"
  default     = "ASIA-SOUTHEAST2"
}

variable "zone" {
  description = "My Project Zone"
  default     = "asia-southeast2-c"
}

variable "gcs_bucket_class" {
  description = "My GCS Bucket Class"
  default     = "STANDARD"
}

variable "project" {
  description = "Project Name"
  default     = "acoustic-portal-411603"
}

variable "project_region" {
  description = "Project Region"
  default     = "asia-southeast2"
}

variable "ssh_public_key" {
  description = "SSH Public Key on Linux"
  # default     = "~/.ssh/gcp-1-ssh-key.pub"    #oman-f28
  # default = "~/.ssh/gcp-oslogin-ssh-key.pub"  #darmawan12
  default = "~/.ssh/google_compute_engine.pub" #darmawan12
}