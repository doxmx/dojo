#!/usr/bin/env bats

# Write your tests here, e.g.

@test "Quotes were added" {
    source kata.sh
    template some message | 
        grep -qP '^".*"$'
}