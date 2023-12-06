i#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me to trigger the desired response
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
