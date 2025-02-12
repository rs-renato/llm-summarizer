#!/bin/bash

# Extract transcriptions from a json file, in this case it's specifics for Zoom meetings.

while getopts t:o: flag
do
    case "${flag}" in
        t) transcription_file="${OPTARG}";;
        o) output_file="${OPTARG}";;
    esac
done

jq -r '.result.transcriptList[] | [.ts, .end_ts, .username, .text] | @tsv' "$transcription_file" | awk '
BEGIN { FS="\t"; OFS=""; last_username="" }
{
    split($1, ts_parts, ":");
    split($2, end_ts_parts, ":");
    ts = sprintf("%02d:%02d:%02d", ts_parts[1], ts_parts[2], ts_parts[3]);
    end_ts = sprintf("%02d:%02d:%02d", end_ts_parts[1], end_ts_parts[2], end_ts_parts[3]);
    username = $3;
    if (username == "") {
        username = last_username;
    } else {
        last_username = username;
    }
    print "[" ts "-" end_ts "][" username "] " $4
}' > "$output_file"
