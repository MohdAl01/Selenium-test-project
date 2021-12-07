import sys 
sys.path.append("C:\\Users\\moham\\Desktop\\python projects\\selenium\\Booking")
from selenium import webdriver 
from constants import *
from booking_filtrations import *
from Booking_report import *
import os
from selenium.webdriver.common.keys import Keys

class Booking(webdriver.Chrome):
	def __init__(self, driver_path=PATH, teardown=False):
		self.driver_path = driver_path
		self.teardown = teardown
		os.environ["PATH"] += self.driver_path
		sys.path.append("C:\\Users\\moham\\Desktop\\python projects\\selenium\\Booking")
		super(Booking, self).__init__()
		self.implicitly_wait(15)
		# self.maximize_window()

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.teardown:
			self.quit()

	def land_first_page(self):
		self.get(BASE_URL)

	def change_currency(self, currency="USD"):
		self.currency = currency 

		currency_element = self.find_element_by_css_selector("button[data-tooltip-text='Choose your currency'")
		currency_element.click()
		

		choose_cur_btn = self.find_element_by_css_selector(f"a[data-modal-header-async-url-param*='selected_currency={currency}']")
		choose_cur_btn.click()

	def input_location(self, place_to_go="moscow"):
		self.place_to_go = place_to_go 

		search_field = self.find_element_by_id("ss")
		search_field.clear()
		search_field.send_keys(place_to_go)

		first_result = self.find_element_by_css_selector('li[data-i="0"]')
		first_result.click()

	def check_in_out(self, check_in_date, check_out_date):
		# format is : year-month-day (e.g 2021-12-21)
		check_in_btn = self.find_element_by_css_selector(
				f'td[data-date="{check_in_date}"]'
			)
		check_in_btn.click()
		check_out_btn = self.find_element_by_css_selector(
				f'td[data-date="{check_out_date}"]'
			)
		check_out_btn.click()

	def select_adults(self, count):
		selection_element = self.find_element_by_id('xp__guests__toggle')
		selection_element.click()
		# whatever, not continuing this 

	def click_search(self):
		search_btn = self.find_element_by_css_selector(
			'button[type="submit"]'
		)
		search_btn.click()

	def apply_filtrations(self):
		filtrations = BookingFiltration(driver=self)
		filtrations.apply_star_rating(5,4,3)
		filtrations.lowest_to_highest()

	def report_results(self):

		properties = self.find_element_by_css_selector(
			'div[data-component="arp-properties-list"]'
		)
		report = BookingReport(properties)
		print(report.pull_deal_box_attributes())