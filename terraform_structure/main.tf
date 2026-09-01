terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "pipeline" {
  name = "pipeline-csv:1.0"

  build {
    context    = ".."
    dockerfile = "Dockerfile.fn_run_pipeline_csv"
  }
}

resource "docker_container" "pipeline" {
  name  = "pipeline-csv"
  image = docker_image.pipeline.image_id
}