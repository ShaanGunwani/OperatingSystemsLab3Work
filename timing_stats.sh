#!/bin/bash



# Run sequential program and capture timing statistics

echo -n "Sequential program" > timing_stats.txt

{ time python3 sequential_count.py input.txt; } 2>> timing_stats.txt



# Run parallel program and capture timing statistics

echo -n "Parallel program" >> timing_stats.txt

{ time python3 parallel_count.py input.txt; } 2>> timing_stats.txt



# Print the timing statistics table

awk '

BEGIN {

    printf "%-20s %-20s %-20s\n", "Program", "Real time", "User time", "System time"

}

{

    if ($0 ~ /real/) {

        real = $2

    } else if ($0 ~ /user/) {

        user = $2

    } else if ($0 ~ /sys/) {

        sys = $2

        printf "%-20s %-20s %-20s\n", program, real, user, sys

    } else if ($0 ~ /Sequential/) {

        program = $1

    } else if ($0 ~ /Parallel/) {

        program = $1

    }

}' timing_stats.txt

