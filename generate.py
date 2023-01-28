from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

from input_items import food_items

# Logo insertion
def insert_company_logo(img, logo_img_path, size, top_offset):
    '''Insert company logo to the top of the receipt'''
    # Getting logo image
    img_logo = Image.open(logo_img_path)
    img_logo = img_logo.resize(size)
    # Find center position
    center_x = int(img.size[0]/2 - img_logo.size[0]/2)
    # Inserting logo
    img.paste(img_logo, (center_x, top_offset), img_logo)

    return img, img_logo

# Header insertion
def insert_header(
                    img,
                    pen, 
                    font_path = '', 
                    font_color = (0,0,0), 
                    company_name = '--', 
                    company_address = '--', 
                    company_contact = '--', 
                    top_offset = 0):
    '''Insert header info'''

    # Company Name
    company_name = company_name[:30]
    font = ImageFont.truetype(font_path, size = 24)
    text_left, text_top, text_right, text_bottom = pen.multiline_textbbox((img.size[0]/2, top_offset), text = company_name, font = font)
    name_text_width = text_right - text_left
    name_text_height = text_bottom - text_top
    center_x = int(img.size[0]/2-name_text_width/2)
    pen.multiline_text((center_x, top_offset), company_name, font=font, fill = font_color, stroke_width=0, align='center')
    # Company Address
    company_name = company_name[:50]
    font = ImageFont.truetype(font_path, size = 16)
    text_left, text_top, text_right, text_bottom = pen.multiline_textbbox((img.size[0]/2, top_offset+name_text_height), text = company_address, font = font)
    address_text_width = text_right - text_left
    address_text_height = text_bottom - text_top
    center_x = int(img.size[0]/2-address_text_width/2)
    spacing = 5
    pen.multiline_text((center_x, (text_top+spacing)), company_address, font=font, fill = font_color, align='center')
    # Company Contact
    company_contact = company_contact[:50]
    font = ImageFont.truetype(font_path, size = 16)
    text_left, text_top, text_right, text_bottom = pen.multiline_textbbox((img.size[0]/2, top_offset+name_text_height+spacing+address_text_height), text = company_contact, font = font)
    contact_text_width = text_right - text_left
    contact_text_height = text_bottom - text_top
    center_x = int(img.size[0]/2-contact_text_width/2)
    spacing = 5
    pen.multiline_text((center_x, (text_top+spacing)), company_contact, font=font, fill = font_color, align='center')
    # Getting header's bottom coordinate for the next content
    bottom_y = (text_top + spacing + contact_text_height)

    return img, bottom_y

def draw_separator(drawer, points, width = 1, fill = (0,0,0)):
    '''Draw a separator line'''
    x1, y1, x2, y2 = points
    drawer.line([x1, y1, x2, y2], fill, width)
    return x1, y2

# Order details insertion
def insert_order_details(
                        pen,
                        font_path = '',
                        font_color = (0,0,0),
                        order_no = '--',
                        order_type = '--',
                        order_date = '--', 
                        order_time = '--', 
                        customer = '--',
                        server = '--',
                        cashier = '--',
                        start_pos_x = 0,
                        start_pos_y = 0, 
                        margin_left = 0, 
                        margin_right=0):
    '''Insert header info'''

    '''Order No.'''
    # Get Order No.
    order_no = order_no[:20]
    text = f'Order No: {order_no}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    y_spacing_before = 5
    x = margin_left
    y = start_pos_y + y_spacing_before
    # Estimate the size and location
    _, _, _, order_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'la')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
    
    '''Order Type'''
    # Get Order No.
    order_type = order_type[:20]
    text = f'Order Type: {order_type}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_right
    # Estimate the size and location
    _, _, _, order_type_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''Date'''
    # Get Order No.
    order_date = order_date[:20]
    text = f'Date: {order_date}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_left
    y_spacing_before = 5
    y = order_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, date_bottom = pen.textbbox(xy = (x, y), text = text, font = font, stroke_width = 1, anchor = 'la')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')

    '''Time'''
    order_time = order_time[:20]
    text = f'Time: {order_time}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_left
    y_spacing_before = 5
    y = date_bottom + y_spacing_before
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')

    '''Customer'''
    customer = customer[:20]
    text = f'Customer: {customer}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = order_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, customer_bottom = pen.textbbox(xy = (x, y), text = text, font = font, stroke_width = 1, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''Server'''
    server = server[:20]
    text = f'Server: {server}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = customer_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, server_bottom = pen.textbbox(xy = (x, y), text = text, font = font, stroke_width = 1, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''Cashier'''
    cashier = cashier[:20]
    text = f'Cashier: {cashier}'
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = server_bottom + y_spacing_before
    # Estimate the size and location
    cashier_left, cashier_top, cashier_right, cashier_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')

    # Returning last x and y position
    return cashier_left, cashier_bottom 

# Order details
def insert_items_header(
                        pen,
                        font_path = '',
                        font_color = (0,0,0),
                        start_pos_x = 0,
                        start_pos_y = 0, 
                        margin_left = 0,
                        margin_right = 0):
    '''Insert items header'''
    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)
    item_headers = ['QTY', 'ITEMS', 'PRICE']

    for header in item_headers:
        text = header
        if header == 'QTY':
            # Positioning
            y_spacing_before = 5
            x = margin_left
            y = start_pos_y + y_spacing_before
            # Writing text
            pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
        elif header == 'ITEMS':
            # Positioning
            shift_left = 50
            x = margin_left + shift_left
            # Writing text
            pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
        elif header == 'PRICE':
            # Positioning
            x = margin_right
            # Writing text
            pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
            # Getting current bottom position
            _, _, _, price_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    
    # Returning last x and y position
    return x, price_bottom
    

def insert_items(items, pen, font_path = '', font_color = (0,0,0), start_pos_y = 0, margin_left=0, margin_right=0):
    '''Inserting food items'''

    # Prepare font
    font = ImageFont.truetype(font_path, size = 16)

    y = start_pos_y
    item_y_spacing = 7
    option_y_spacing = 5

    for item in items:
        # Put spacing between items
        y = y + item_y_spacing
        for key in item.keys():
            if key == 'qty':
                item_qty = item[key]
                text = str(item_qty)
                # Positioning
                x = margin_left
                # Writing
                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
            elif key == 'name':
                text = item[key]
                # Positioning
                shift_left = 50
                x = margin_left + shift_left
                # Writing
                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
            elif key == 'price':
                item_price = item[key] * item_qty
                text = f'${item_price}'
                # Positioning
                x = margin_right
                # Writing
                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
                # Getting current bottom position
                _, _, _, bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
                y = bottom

            elif key == 'options':
                options = item[key]
                if len(options) == 0:
                    # There is no options
                    continue
                else:
                    # There are option, enumerate and print it
                    for opt in options:
                        # Put spacing between items
                        y = y + option_y_spacing
                        for opt_key in opt.keys():
                            if opt_key == 'qty':
                                opt_qty = opt[opt_key]
                                text = f'{opt_qty}'
                                # Positioning
                                x = margin_left
                                # Writing
                                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
                            elif opt_key == 'name':
                                text = f'OPT: {opt[opt_key]}'
                                # Positioning
                                shift_left = 70
                                x = margin_left + shift_left
                                # Writing
                                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'la')
                            elif opt_key == 'price':
                                opt_price = opt[opt_key] * opt_qty
                                text = f'${opt_price}'
                                # Positioning
                                x = margin_right
                                # Writing
                                pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
                                # Getting current bottom position
                                _, _, _, bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
                                y = bottom
    return x, y

# Price and payment
def insert_price_payment(
                        pen,
                        font_path = '',
                        font_color = (0,0,0),
                        subtotal_price = 0,
                        tax_percent = 0,
                        tax = 0,
                        total_price = 0,
                        payment = 0,
                        change = 0,
                        payment_method = '--',
                        start_pos_x = 0,
                        start_pos_y = 0, 
                        margin_left = 0,
                        margin_right = 0):
    '''Insert price and payment section'''

    # Prepare font
    font = ImageFont.truetype(font_path, size = 18)

    '''Subtotal'''
    text = f'${subtotal_price}'
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = start_pos_y + y_spacing_before
    # Estimate the size and location
    _, _, _, subtotal_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Subtotal text
    text = f'Subtotal:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''Tax'''
    text = f'${tax}'
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = subtotal_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, tax_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Tax text
    text = f'Tax:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''Total'''
    text = f'${total_price}'
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = tax_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, total_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Total text
    text = f'Total:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''payment'''
    text = f'${payment}'
    # Positioning
    x = margin_right
    y_spacing_before = 30
    y = total_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, payment_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Tendered text
    text = f'Tendered:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''change'''
    text = f'${change}'
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = payment_bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, change_bottom = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Change text
    text = f'Change:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    '''payment method'''
    '''Writing payment method text'''
    text = 'Payment Methods'
    # Positioning
    x = margin_right
    y_spacing_before = 5
    y = change_bottom + y_spacing_before
    # Estimate the size and location
    _left, top_, _right, _bottom  = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Draw line
    draw_separator(pen, points = [_left, _bottom , _right, _bottom], width = 1)
    '''Writing payment method values'''
    text = f'${payment}'
    # Positioning
    x = margin_right
    y_spacing_before = 7
    y = _bottom + y_spacing_before
    # Estimate the size and location
    _, _, _, _payment_method_bottom  = pen.textbbox(xy = (x, y), text = text, font = font, anchor = 'ra')
    # Writing text
    pen.text(xy = (x, y), text = text, font = font, fill = font_color, anchor = 'ra')
    # Writing Payment Method text
    text = f'{payment_method}:'
    pen.text(xy = (x - 120, y), text = text, font = font, fill = font_color, anchor = 'ra')

    # Returning last x and y position
    return x, _payment_method_bottom

# Footer insertion
def insert_footer(
                    pen, 
                    font_path = '', 
                    font_color = (0,0,0), 
                    message = 'Thank you, come again!', 
                    customer_sequence = 1,
                    start_pos_x = 0,
                    start_pos_y = 0, 
                    margin_left = 0,
                    margin_right = 0):
    '''Insert footer'''

    '''Message'''
    font = ImageFont.truetype(font_path, size = 18)
    text = message
    # Estimating bounding box
    msg_left, _, msg_right, msg_bottom = pen.textbbox((img.size[0]/2, start_pos_y), text = text, font = font)
    msg_width = msg_right - msg_left
    # Positioning relative to previouse section
    center_x = int(img.size[0]/2 - msg_width/2)
    # Writing
    pen.text((center_x, start_pos_y), text, font=font, fill = font_color)   
    
    '''Customer sequence'''
    font = ImageFont.truetype(font_path, size = 32)
    text = f'**  {customer_sequence}  **'
    # Estimating bounding box
    seq_left, _, seq_right, _ = pen.textbbox((img.size[0]/2, msg_bottom), text = text, font = font)
    seq_width = seq_right - seq_left
    # Positioning relative to message
    center_x = int(img.size[0]/2 - seq_width/2)
    y_spacing_before = 10
    y = msg_bottom + y_spacing_before
    # Writing
    pen.text((center_x, y), text, font=font, fill = font_color)    

def calculate_item_rows(items):
    # Calculate number of item rows
    rows = 0
    for item in items:
        rows += 1
        options = item['options']
        n_option = len(options)
        if n_option > 0:
            rows += n_option
    return rows

def calculate_total_price(items, tax_percent):
    # Calculate total price
    subtotal_price = 0
    for item in items:
        # Price for item
        item_qty = item['qty']
        item_price = item['price']
        subtotal_price += item_price * item_qty
        # Price for option
        options = item['options']
        n_option = len(options)
        if n_option > 0:
            for option in options:
                option_qty = option['qty']
                option_price = option['price']
                subtotal_price += option_price * option_qty

    # Tax component
    tax = subtotal_price*(tax_percent)/100
    # Total price
    total_price = subtotal_price + tax

    # Return subtotal, tax percentage and total price
    return (subtotal_price, tax, total_price)



'''Input data'''
items = food_items

'''Price and payment processing'''
# Tax
tax_percent = 13
# Price
subtotal_price, tax, total_price = calculate_total_price(items, tax_percent = tax_percent)
# Payment
tendered = 100
payment_method = 'CASH'
# Change calculation
change = tendered - total_price
# String formatting
subtotal_price = '%.2f' % round(subtotal_price, 2)
tax = '%.2f' % round(tax,2)
total_price = '%.2f' % round(total_price, 2)
tendered = '%.2f' % round(tendered, 2)
change = '%.2f' % round(change, 2)


''' Receipt Image Generation'''
# Size
dpi = 180
mm_pixel_multiplier = 7
width_mm = 70
# Top section height
top_height_mm = 45
# Content section height
mm_per_item = 4
n_rows = calculate_item_rows(items)
content_height_mm =  int(n_rows * mm_per_item)
# Bottom section height
bottom_height_mm = 45
height_mm = top_height_mm + content_height_mm + bottom_height_mm
image_size = (width_mm * mm_pixel_multiplier, height_mm * mm_pixel_multiplier)

# Offset and margins
top_offset_px = 20
margin_left = 20
margin_right = image_size[0]-20

# Font
font_color = (0,0,0)
font_path = 'fonts/arial.ttf'
# Company Info
company_logo_path = 'images/test_logo.png'
company_name = 'Company Name'
company_address = 'Company address, street, city, country'
company_contact = 'Phone: +12 345 678910, Tax No.: 12345678910'
# Order Details
order_no = '123456'
order_type = 'Dine-In'

# Date and time
now = datetime.now()
date = now.strftime('%d-%m-%y')
time = now.strftime('%H:%M')

# Image
bg_color = (255, 255, 255)
# Create an initial image
img = Image.new('RGB', image_size, bg_color)
# Create drawing object
pen = ImageDraw.Draw(img)
# Load font
font = ImageFont.truetype(font_path, size = 24)


# Inserting logo
img, img_logo = insert_company_logo(img, company_logo_path, (90,65), 20)
# Inserting header
spacing_from_logo = 20
header_offset = top_offset_px + img_logo.size[1] + spacing_from_logo
img, header_bottom = insert_header(img, pen, font_path, font_color, company_name, company_address, company_contact, header_offset)
# Drawing separator
spacing_from_header = 20
cursor_pos_x, cursor_pos_y = draw_separator(pen, points = [margin_left, header_bottom + spacing_from_header, margin_right, header_bottom + spacing_from_header], width = 2)
# Insert order details
cursor_pos_x, cursor_pos_y = insert_order_details(
                                                    pen,
                                                    font_path, 
                                                    font_color, 
                                                    order_no = order_no,
                                                    order_type = order_type,
                                                    order_date = date,
                                                    order_time = time,
                                                    customer = 'Mr. Customer',
                                                    server = 'Ms. Server',
                                                    cashier = 'Ms. Cashier',
                                                    start_pos_x = cursor_pos_x,
                                                    start_pos_y = cursor_pos_y,
                                                    margin_left = margin_left,
                                                    margin_right = margin_right
                                                    )
# Drawing separator
spacing_y = 10
cursor_pos_x, cursor_pos_y = draw_separator(pen, points = [margin_left, cursor_pos_y + spacing_y, margin_right, cursor_pos_y + spacing_y], width = 4)

# Insert item header
spacing_y = 10
cursor_pos_x, cursor_pos_y = insert_items_header(pen, font_path, font_color, start_pos_x = 0, start_pos_y = (cursor_pos_y + spacing_y), margin_left = margin_left, margin_right = margin_right)

# Insert food items
spacing_y = 10
cursor_pos_x, cursor_pos_y = insert_items(items, pen, font_path, font_color, start_pos_y = (cursor_pos_y + spacing_y), margin_left = margin_left, margin_right = margin_right)

# Drawing separator
spacing_y = 10
cursor_pos_x, cursor_pos_y = draw_separator(pen, points = [margin_left, cursor_pos_y + spacing_y, margin_right, cursor_pos_y + spacing_y], width = 2)

# Insert price and payment
spacing_y = 10
cursor_pos_x, cursor_pos_y = insert_price_payment(
                                                    pen, 
                                                    font_path,
                                                    font_color, 
                                                    subtotal_price = subtotal_price, 
                                                    tax_percent = tax_percent, 
                                                    tax = tax, 
                                                    total_price = total_price, 
                                                    payment = tendered, 
                                                    payment_method = payment_method,
                                                    change = change,
                                                    start_pos_y = (cursor_pos_y + spacing_y), 
                                                    margin_left = margin_left, 
                                                    margin_right = margin_right
                                                )

# Drawing separator
spacing_y = 20
cursor_pos_x, cursor_pos_y = draw_separator(pen, points = [margin_left, cursor_pos_y + spacing_y, margin_right, cursor_pos_y + spacing_y], width = 4)

# Insert footer
spacing_y = 30
insert_footer(
                pen, 
                font_path,
                font_color, 
                message = 'Thank you, come again!', 
                customer_sequence = 123,
                start_pos_y = (cursor_pos_y + spacing_y)
            )

# Test saving
img.save('test.png')


