from lib import extract_date_from_filename

# Example usage of extract_date_from_filename
# Given the filename 'aaaa241113_10_09.log', it would return:
# ('241113', '1009')
def test_extract_date_from_filename():
    test_cases = [
        ('aaaa241113_10_09.log', ('241113', '1009')),
        ('file010120_12_30.txt', ('010120', '1230')),
        ('report311219_23_59.log', ('311219', '2359')),
        ('data010101_00_00.txt', ('010101', '0000')),
        ('no_date_file.txt', (None, None)),
        ('invalid_date123.log', (None, None)),
        ('anotherfile010203_12_34.log', ('010203', '1234')),
    ]
    
    for filename, expected in test_cases:
        result = extract_date_from_filename(filename)
        assert result == expected, f"Failed for {filename}: expected {expected}, got {result}"
    
    print("All tests passed!")

# Example usage
# test_extract_date_from_filename()

if __name__ == "__main__":
    test_extract_date_from_filename()