#!/bin/bash

export __dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export __dir="$( dirname ${__dir} )"

command -v virtualenv >/dev/null 2>&1 || { echo >&2 "I require \`virtualenv\` but it's not installed. Aborting."; exit 1; }

if [ ! -d ${__dir}/__envi ]
then
    virtualenv ${__dir}/__envi
fi

. ${__dir}/__envi/bin/activate

set -x

${__dir}/__envi/bin/pip install --upgrade distribute
${__dir}/__envi/bin/pip install --upgrade -r ${__dir}/requirements.txt
