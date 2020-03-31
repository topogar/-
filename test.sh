#!/bin/bash

set -m
yarn start &

pytest ./tests
