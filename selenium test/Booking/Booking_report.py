# includes methods that parse data from deal boxes

class BookingReport:
	def __init__(self, boxes_section_element):
		self.boxes_section_element = boxes_section_element
		self.deal_boxes = self.pull_deal_boxes()

	def pull_deal_boxes(self):

		return self.boxes_section_element.find_elements_by_css_selector(
			'div[data-testid="property-card"]'
		)

	def pull_deal_box_attributes(self):
		collection = []

		for deal_box in self.deal_boxes:
			hotel_name = deal_box.find_element_by_css_selector(
				'div[data-testid="title"]'
			).get_attribute("innerHTML").strip()

			prices = []
			hotel_price = deal_box.find_element_by_css_selector(
				'div[data-testid="price-and-discounted-price"]'
			)
			for whatever in hotel_price.find_element_by_css_selector("*"):
				bad_name = whatever.get_attribute("innerHTML").strip()
				prices.append(bad_name)
			collection.append(
				[hotel_name, prices]
			)
		return collection