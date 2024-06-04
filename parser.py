import re
from xml.etree.ElementTree import Element, SubElement, tostring

# Regular expression to match struct definitions
struct_pattern = re.compile(r'typedef struct\s*{\s*([^}]+)\s*}\s*(\w+);')

# Regular expression to match fields within a struct
field_pattern = re.compile(r'(\w+)\s+(\w+)(\[\d+\])?;')

# Parse the structure.h file
with open('structure.h', 'r') as file:
    content = file.read()

structs = struct_pattern.findall(content)

# Constants for window dimensions
MAX_WINDOW_WIDTH = 1200
MAX_WINDOW_HEIGHT = 800
FIELD_WIDTH = 150  # Fixed width of each field
FIELD_HEIGHT = 30  # Fixed height of each field
FIELD_SPACING = 10  # Spacing between fields

# Function to create GTK Builder XML elements
def create_gtk_xml(structs):
    root = Element('interface')

    # Create the main window
    main_window = SubElement(root, 'object', {'class': 'GtkWindow', 'id': 'main_window'})
    window_prop = SubElement(main_window, 'property', {'name': 'title'})
    window_prop.text = 'Structs GUI'
    main_grid = SubElement(main_window, 'child')
    main_grid_obj = SubElement(main_grid, 'object', {'class': 'GtkGrid', 'id': 'main_grid'})
    main_grid_row_spacing = SubElement(main_grid_obj, 'property', {'name': 'row-spacing'})
    main_grid_row_spacing.text = '20'
    main_grid_column_spacing = SubElement(main_grid_obj, 'property', {'name': 'column-spacing'})
    main_grid_column_spacing.text = '20'

    # Calculate the number of structs that can fit horizontally and vertically
    num_columns = MAX_WINDOW_WIDTH // (FIELD_WIDTH + FIELD_SPACING)
    num_rows = MAX_WINDOW_HEIGHT // (FIELD_HEIGHT + FIELD_SPACING)

    for index, (fields, struct_name) in enumerate(structs):
        # Determine position in the grid
        row = index // num_columns
        column = index % num_columns

        # Create a box for each struct
        frame = SubElement(main_grid_obj, 'child')
        frame_obj = SubElement(frame, 'object', {'class': 'GtkFrame', 'id': f'{struct_name}_frame'})
        label = SubElement(frame_obj, 'property', {'name': 'label'})
        label.text = struct_name

        box = SubElement(frame_obj, 'child')
        box_obj = SubElement(box, 'object', {'class': 'GtkBox', 'id': f'{struct_name}_box'})
        box_orientation = SubElement(box_obj, 'property', {'name': 'orientation'})
        box_orientation.text = 'vertical'
        box_spacing = SubElement(box_obj, 'property', {'name': 'spacing'})
        box_spacing.text = str(FIELD_SPACING)

        field_lines = fields.strip().split('\n')
        for i, line in enumerate(field_lines):
            field_match = field_pattern.match(line.strip())
            if field_match:
                field_type, field_name, field_array = field_match.groups()
                unique_label_id = f'{struct_name}_{field_name}_label'
                unique_entry_id = f'{struct_name}_{field_name}_entry'

                # Create a box for each field
                field_box = SubElement(box_obj, 'child')
                field_box_obj = SubElement(field_box, 'object', {'class': 'GtkBox', 'id': f'{struct_name}_{field_name}_box'})
                field_box_orientation = SubElement(field_box_obj, 'property', {'name': 'orientation'})
                field_box_orientation.text = 'horizontal'
                field_box_spacing = SubElement(field_box_obj, 'property', {'name': 'spacing'})
                field_box_spacing.text = '5'

                # Create a label for the field
                label = SubElement(field_box_obj, 'child')
                label_obj = SubElement(label, 'object', {'class': 'GtkLabel', 'id': unique_label_id})
                prop_label = SubElement(label_obj, 'property', {'name': 'label'})
                prop_label.text = field_name
                label_width = SubElement(label_obj, 'property', {'name': 'width-request'})
                label_width.text = str(FIELD_WIDTH)
                label_height = SubElement(label_obj, 'property', {'name': 'height-request'})
                label_height.text = str(FIELD_HEIGHT)

                # Create an appropriate entry widget for the field type
                entry = SubElement(field_box_obj, 'child')
                if field_type in ['int8_t', 'int16_t', 'int32_t', 'int64_t']:
                    entry_obj = SubElement(entry, 'object', {'class': 'GtkSpinButton', 'id': unique_entry_id})
                elif field_type in ['float', 'double']:
                    entry_obj = SubElement(entry, 'object', {'class': 'GtkScale', 'id': unique_entry_id})
                else:
                    entry_obj = SubElement(entry, 'object', {'class': 'GtkEntry', 'id': unique_entry_id})
                entry_width = SubElement(entry_obj, 'property', {'name': 'width-request'})
                entry_width.text = str(FIELD_WIDTH)
                entry_height = SubElement(entry_obj, 'property', {'name': 'height-request'})
                entry_height.text = str(FIELD_HEIGHT)

        # Set the position of the frame in the main grid
        frame_packing = SubElement(frame, 'packing')
        frame_left_attach = SubElement(frame_packing, 'property', {'name': 'left-attach'})
        frame_left_attach.text = str(column)
        frame_top_attach = SubElement(frame_packing, 'property', {'name': 'top-attach'})
        frame_top_attach.text = str(row)

    return tostring(root, encoding='unicode', method='xml')

# Generate the GTK Builder XML
gtk_xml = create_gtk_xml(structs)

# Write the GTK Builder XML to a file
with open('gui.glade', 'w') as file:
    file.write(gtk_xml)

print("GTK Builder XML file generated as 'gui.glade'")
