#!/bin/sh
# Resolve the sentence-transformers embedding model to a concrete local
# snapshot directory inside the bind-mounted HuggingFace cache.
#
# Why: with HF_HUB_OFFLINE=1 on a Windows-hosted cache, resolving the repo-id
# ("all-mpnet-base-v2") fails HF's cache validation, but loading the snapshot
# directory directly works. We discover the snapshot dynamically so the setup
# survives a future cache refresh (the commit hash changes).

set -e

HF_HUB_DIR="${HF_HOME:-/root/.cache/huggingface}/hub"
MODEL_GLOB="$HF_HUB_DIR/models--sentence-transformers--all-mpnet-base-v2/snapshots"

# If EMBEDDING_MODEL is unset or a bare repo id, try to resolve a snapshot dir.
case "$EMBEDDING_MODEL" in
  "" | all-mpnet-base-v2 | sentence-transformers/all-mpnet-base-v2)
    SNAP=$(find "$MODEL_GLOB" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | head -n 1 || true)
    if [ -n "$SNAP" ]; then
      export EMBEDDING_MODEL="$SNAP"
      echo "[entrypoint] Using embedding model from cache: $EMBEDDING_MODEL"
    else
      echo "[entrypoint] No cached snapshot found; falling back to online repo id."
    fi
    ;;
esac

exec "$@"
