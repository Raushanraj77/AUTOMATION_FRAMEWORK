#!/bin/bash

# Constants
MAX_RETRIES=3
RETRY_FILE="rerun.txt"
RESULT_DIR="reports/allure-results"
ALLURE_ATTEMPT_DIR="reports/attempt_results"
MERGED_RESULTS="reports/merged-results"
TRACK_FILE="$MERGED_RESULTS/alltest.txt"
SCREENSHOTS="screenshots"

# Clean previous outputs
rm -rf "$RESULT_DIR" "$RETRY_FILE" "$ALLURE_ATTEMPT_DIR" "$MERGED_RESULTS" "$SCREENSHOTS"
#Create required folders
mkdir -p "$RESULT_DIR" "$ALLURE_ATTEMPT_DIR" "$MERGED_RESULTS"
echo "✨ Starting initial test run..."
# Initial run
behave \
  -f allure_behave.formatter:AllureFormatter \
  -o "$RESULT_DIR" \
  features

# Save first attempt results
cp -r "$RESULT_DIR" "$ALLURE_ATTEMPT_DIR/attempt1"

# Retry loop
for i in $(seq 2 $MAX_RETRIES); do
  echo -e "\n🔄 Retry Attempt $i"
  if [ -s "$RETRY_FILE" ]; then
    behave @"$RETRY_FILE" \
      -f allure_behave.formatter:AllureFormatter \
      -o "$ALLURE_ATTEMPT_DIR/attempt$i"

    echo "✅ Attempt $i completed."
  else
    echo "✅ All tests passed after attempt $((i - 1))"
    break
  fi
done

# ✅ Merging results: Only unique .uuid
echo "📦 Merging unique Allure test results..."
#!/bin/bash
#Clear content of file
> "$TRACK_FILE"
# Loop through all attempt folders
for dir in "$ALLURE_ATTEMPT_DIR"/attempt*/; do
  if [ -d "$dir" ]; then
    echo "🔍 Scanning $dir"

    for file in "$dir"/*.json; do
      name=$(jq -r '.name // empty' "$file")
      status=$(jq -r '.status // empty' "$file")
      filepath=$(realpath "$file")

      if [[ -z "$name" || "$status" == "null" ]]; then
        continue
      fi

      # Check if name is already present in alltest.txt
      existing_entry=$(grep -F "|$name|" "$TRACK_FILE")

      if [[ -z "$existing_entry" ]]; then
        # Not seen before → add to list and copy
        echo "$status|$name|$filepath" >> "$TRACK_FILE"
        cp "$filepath" "$RESULT_DIR/"
        echo "✅ Added new test: $name ($status)"
      else
        existing_status=$(echo "$existing_entry" | cut -d'|' -f1)

        if [[ "$existing_status" != "passed" && "$status" == "passed" ]]; then
          # If old status was failed/skipped and this is passed, update
          sed -i "/|$name|/d" "$TRACK_FILE"
          echo "$status|$name|$filepath" >> "$TRACK_FILE"
          cp "$filepath" "$RESULT_DIR/"
          echo "🔁 Updated $name to PASSED"
        fi
      fi
    done
  fi
done
echo "🎉 Merge completed to $TRACK_FILE" 
# ======================
# Generate Final Allure Report
# ======================
echo "📊 Launching merged Allure report..."
allure serve "$RESULT_DIR"
