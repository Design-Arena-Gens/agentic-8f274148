<?php
// Task 1: Find the largest of three numbers using nested if

echo "=== Finding Largest of Three Numbers ===\n\n";

// Input three numbers
$num1 = 45;
$num2 = 78;
$num3 = 62;

echo "Number 1: $num1\n";
echo "Number 2: $num2\n";
echo "Number 3: $num3\n\n";

// Find largest using nested if
if ($num1 >= $num2) {
    if ($num1 >= $num3) {
        $largest = $num1;
    } else {
        $largest = $num3;
    }
} else {
    if ($num2 >= $num3) {
        $largest = $num2;
    } else {
        $largest = $num3;
    }
}

echo "The largest number is: $largest\n";
?>
