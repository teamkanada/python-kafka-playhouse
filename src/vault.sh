#!/bin/sh

function entrypoint () {
  VAULT_DIR="/vault/secrets"
  if [ -d ${VAULT_DIR} ]; then
    # Set environment from env secrets
    SECRETS=$(cat ${VAULT_DIR}/env-* | xargs)
    exec env $SECRETS $@
  else
    exec $@
  fi
}
