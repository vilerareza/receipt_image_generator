from receipt_generator import ReceiptGenerator
from input_items import food_items, company_info, order_info, price_payment_info

receipt_generator = ReceiptGenerator()
out_file_path = f"./output/Receipt_{order_info['order_no']}.png"

if __name__ == "__main__":
    img = receipt_generator.generate(food_items, company_info, order_info, price_payment_info)
    img.save(out_file_path)
