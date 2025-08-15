#!/bin/sh

if [ ! -f "$LIVENESS_FILE" ]; then
  echo "❌ Liveness file missing: $LIVENESS_FILE"
  exit 1
fi

NEXT_CHECK=$(cat "$LIVENESS_FILE" 2>/dev/null)
NOW=$(date +%s)

if [ -z "$NEXT_CHECK" ]; then
  echo "❌ Liveness file is empty or unreadable"
  exit 1
fi

if [ "$NOW" -gt "$NEXT_CHECK" ]; then
  echo "❌ Liveness overdue – now=$NOW > expected=$NEXT_CHECK"
  exit 1
fi

echo "✅ Liveness OK – now=$NOW <= expected=$NEXT_CHECK"
exit 0
