#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle, Preformatted
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

def create_pdf():
    # Create PDF
    pdf_filename = "PHP_Programming_Project.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                            topMargin=0.75*inch, bottomMargin=0.75*inch,
                            leftMargin=1*inch, rightMargin=1*inch)

    # Container for the 'Flowable' objects
    elements = []

    # Define custom styles
    styles = getSampleStyleSheet()

    # Title style for front page
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Subtitle style
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#333333'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )

    # Task title style
    task_title_style = ParagraphStyle(
        'TaskTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    # Section heading style
    section_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=10,
        spaceBefore=15,
        fontName='Helvetica-Bold'
    )

    # Normal text style
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )

    # Code style
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=9,
        textColor=colors.HexColor('#000000'),
        spaceAfter=12,
        leftIndent=20,
        fontName='Courier'
    )

    # ==================== FRONT PAGE ====================
    elements.append(Spacer(1, 1.5*inch))

    # Main Title
    elements.append(Paragraph("PHP PROGRAMMING", title_style))
    elements.append(Paragraph("PROJECT REPORT", title_style))
    elements.append(Spacer(1, 0.5*inch))

    # Subtitle
    elements.append(Paragraph("Practical Implementation of PHP Programs", subtitle_style))
    elements.append(Spacer(1, 1*inch))

    # Project details table
    project_data = [
        ['Subject:', 'PHP Programming'],
        ['Total Tasks:', '2'],
        ['Date:', 'November 2025'],
    ]

    project_table = Table(project_data, colWidths=[2*inch, 4*inch])
    project_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))

    elements.append(project_table)
    elements.append(PageBreak())

    # ==================== TASK 1 ====================
    elements.append(Paragraph("TASK 1", task_title_style))
    elements.append(Spacer(1, 0.2*inch))

    # Task Name
    elements.append(Paragraph("Task Name", section_style))
    elements.append(Paragraph("Find the Largest of Three Numbers Using Nested If", normal_style))

    # AIM
    elements.append(Paragraph("AIM", section_style))
    elements.append(Paragraph(
        "To write a PHP program that accepts three numbers as input and determines "
        "the largest among them using nested if-else statements.",
        normal_style
    ))

    # Problem Statement
    elements.append(Paragraph("Problem Statement", section_style))
    elements.append(Paragraph(
        "Given three numbers, we need to compare them and find which one is the largest. "
        "The comparison should be done using nested if-else conditional statements to "
        "demonstrate the control flow in PHP programming.",
        normal_style
    ))

    # Constraints
    elements.append(Paragraph("Constraints", section_style))
    elements.append(Paragraph("• The program accepts three numeric values (integer or float)", normal_style))
    elements.append(Paragraph("• Comparison must be performed using nested if statements only", normal_style))
    elements.append(Paragraph("• The program should handle equal numbers correctly", normal_style))

    # Procedure
    elements.append(Paragraph("Procedure", section_style))
    elements.append(Paragraph("1. Declare and initialize three variables with numeric values", normal_style))
    elements.append(Paragraph("2. Display the input numbers", normal_style))
    elements.append(Paragraph("3. Use the first if statement to compare the first two numbers", normal_style))
    elements.append(Paragraph("4. Use nested if statements to compare with the third number", normal_style))
    elements.append(Paragraph("5. Store the largest number in a variable", normal_style))
    elements.append(Paragraph("6. Display the largest number as output", normal_style))

    # Program
    elements.append(Paragraph("Program", section_style))

    task1_code = '''<?php
// Task 1: Find the largest of three numbers using nested if

echo "=== Finding Largest of Three Numbers ===\\n\\n";

// Input three numbers
$num1 = 45;
$num2 = 78;
$num3 = 62;

echo "Number 1: $num1\\n";
echo "Number 2: $num2\\n";
echo "Number 3: $num3\\n\\n";

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

echo "The largest number is: $largest\\n";
?>'''

    elements.append(Preformatted(task1_code, code_style))

    # Output
    elements.append(Paragraph("Output", section_style))

    task1_output = '''=== Finding Largest of Three Numbers ===

Number 1: 45
Number 2: 78
Number 3: 62

The largest number is: 78'''

    # Create output box
    output_data = [[task1_output]]
    output_table = Table(output_data, colWidths=[6.5*inch])
    output_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f5f5f5')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(output_table)
    elements.append(Spacer(1, 0.15*inch))

    # Conclusion
    elements.append(Paragraph("Conclusion", section_style))
    elements.append(Paragraph(
        "The PHP program successfully determines the largest of three numbers using nested "
        "if-else statements. The program demonstrates proper use of conditional logic and "
        "control flow. In this execution, among the three numbers 45, 78, and 62, the program "
        "correctly identified 78 as the largest number. This approach can be extended to handle "
        "user input and validate data types for robust applications.",
        normal_style
    ))

    elements.append(PageBreak())

    # ==================== TASK 2 ====================
    elements.append(Paragraph("TASK 2", task_title_style))
    elements.append(Spacer(1, 0.2*inch))

    # Task Name
    elements.append(Paragraph("Task Name", section_style))
    elements.append(Paragraph("Reverse a String Using strrev() Function", normal_style))

    # AIM
    elements.append(Paragraph("AIM", section_style))
    elements.append(Paragraph(
        "To write a PHP program that reverses a given string using the built-in strrev() function.",
        normal_style
    ))

    # Problem Statement
    elements.append(Paragraph("Problem Statement", section_style))
    elements.append(Paragraph(
        "Given a string input, we need to reverse the order of characters in the string. "
        "PHP provides a built-in function strrev() that performs this operation efficiently. "
        "The task is to demonstrate the usage of this function with a sample string.",
        normal_style
    ))

    # Constraints
    elements.append(Paragraph("Constraints", section_style))
    elements.append(Paragraph("• The input must be a valid string", normal_style))
    elements.append(Paragraph("• The strrev() function must be used for reversal", normal_style))
    elements.append(Paragraph("• Both original and reversed strings should be displayed", normal_style))

    # Procedure
    elements.append(Paragraph("Procedure", section_style))
    elements.append(Paragraph("1. Declare and initialize a string variable with a text value", normal_style))
    elements.append(Paragraph("2. Display the original string", normal_style))
    elements.append(Paragraph("3. Use the strrev() function to reverse the string", normal_style))
    elements.append(Paragraph("4. Store the reversed string in a new variable", normal_style))
    elements.append(Paragraph("5. Display the reversed string as output", normal_style))

    # Program
    elements.append(Paragraph("Program", section_style))

    task2_code = '''<?php
// Task 2: Reverse a string using strrev()

echo "=== String Reversal using strrev() ===\\n\\n";

// Input string
$originalString = "Hello World PHP Programming";

echo "Original String: $originalString\\n";

// Reverse the string using strrev()
$reversedString = strrev($originalString);

echo "Reversed String: $reversedString\\n";
?>'''

    elements.append(Preformatted(task2_code, code_style))

    # Output
    elements.append(Paragraph("Output", section_style))

    task2_output = '''=== String Reversal using strrev() ===

Original String: Hello World PHP Programming
Reversed String: gnimmargorP PHP dlroW olleH'''

    # Create output box
    output_data2 = [[task2_output]]
    output_table2 = Table(output_data2, colWidths=[6.5*inch])
    output_table2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f5f5f5')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('BOX', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(output_table2)
    elements.append(Spacer(1, 0.15*inch))

    # Conclusion
    elements.append(Paragraph("Conclusion", section_style))
    elements.append(Paragraph(
        "The PHP program successfully reverses the input string using the strrev() function. "
        "The strrev() function is a built-in PHP string manipulation function that efficiently "
        "reverses the character order of a string. In this execution, the string 'Hello World PHP Programming' "
        "was successfully reversed to 'gnimmargorP PHP dlroW olleH'. This function is particularly "
        "useful in various string processing tasks, data validation, and text manipulation applications.",
        normal_style
    ))

    # Build PDF
    doc.build(elements)
    print(f"PDF generated successfully: {pdf_filename}")
    return pdf_filename

if __name__ == "__main__":
    create_pdf()
