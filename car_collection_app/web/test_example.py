import re
from playwright.sync_api import Page, sync_playwright, expect

# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")

#     # Expect a title "to contain" a substring.
#     expect(page).to_have_title(re.compile("Playwright"))

# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_homepage_view(page: Page):
    page.goto("https://car-collection-app.onrender.com/")
    expect(page).to_have_title(re.compile("CarCollection"))
    expect(page).to_have_url(re.compile("https://car-collection-app.onrender.com/"))
    page.get_by_text("CARS COLLECTION")
    expect(page.get_by_text("Create Profile")).to_be_visible()
    page.get_by_role("link", name="Create Profile").click()
   
def test_create_profile_view(page: Page):
    page.goto("https://car-collection-app.onrender.com/")
    expect(page.get_by_text("Create Profile")).to_be_visible()
    page.get_by_role("link", name="Create Profile").click()

    page.get_by_text("Create Profile")
    expect(page.get_by_role("heading", name="Create Profile")).to_be_visible()

def test_create_profile_form(page: Page):
    page.goto("https://car-collection-app.onrender.com/profile/create/")
    expect(page).to_have_url(re.compile("https://car-collection-app.onrender.com/profile/create/"))

    
    
    expect(page.get_by_text("Username:")).to_be_visible()
    expect(page.get_by_text("Email:")).to_be_visible()
    expect(page.get_by_text("Age:")).to_be_visible()
    expect(page.get_by_text("Password:")).to_be_visible()	
    expect(page.get_by_role("link", name="Create Profile")).to_be_visible()

def test_create_profile(page: Page):
    page.goto("https://car-collection-app.onrender.com/profile/create/")	
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("test_user")
	
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("test@email.com")
	
    page.get_by_label("Age:").click()
    page.get_by_label("Age:").fill("23")

    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("123")
    page.get_by_role("button", name="Create Profile").click()



    expect(page.get_by_text("No cars yet")).to_be_visible(timeout=3000) 

def test_create_car_view(page: Page):
    page.goto("https://car-collection-app.onrender.com/catalogue/")
    expect(page.get_by_text("Create Car")).to_be_visible()
    expect(page.get_by_role("link", name="Create Car")).to_be_visible()
    expect(page.get_by_text("Create Car")).to_be_visible()
    page.get_by_role("link", name="Create Car").click()
    expect(page.get_by_text("Type:")).to_be_visible()
    expect(page.get_by_text("Model:")).to_be_visible()
    expect(page.get_by_text("Year:")).to_be_visible()
    expect(page.get_by_text("Image url:")).to_be_visible()
    expect(page.get_by_text("Price:")).to_be_visible()

def test_input_fields(page: Page):
    page.goto("https://car-collection-app.onrender.com/car/create/")
    # expect(page.get_by_text("Create Car")).to_be_visible()
    expect(page.get_by_role("heading", name="Create Car")).to_be_visible()

    
    page.get_by_label("Type:").click()
    page.get_by_label("Type:").select_option("Other")
    
    page.get_by_label("Model:").click()
    page.get_by_label("Model:").fill("Test")
    
    page.get_by_label("Year:").click()
    page.get_by_label("Year:").fill("2020")
    
    page.get_by_label("Image url:").click()
    page.get_by_label("Image url:").fill("https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg")

    page.get_by_label("Price:").click()
    page.get_by_label("Price:").fill("12.345")
    page.get_by_role("button", name="Create Car").click()
   
def test_edit_car_view(page: Page):
    page.goto("https://car-collection-app.onrender.com/catalogue/")
    page.get_by_role("link", name="Details").click()
    page.get_by_role("heading", name="Car Details").click()
    page.get_by_role("link", name="Edit").click()
    page.get_by_label("Price:").click()
    page.get_by_label("Price:").fill("12.666")
    page.get_by_role("button", name="Edit Car").click()

def test_edited_car_price(page: Page):
    page.goto("https://car-collection-app.onrender.com/catalogue/")
    page.get_by_role("link", name="Details").click()
    page.get_by_role("heading", name="Car Details").click()
    expect(page.get_by_text("Price: 12.666")).to_be_visible()

def test_delete_car_view(page: Page):  
    page.goto("https://car-collection-app.onrender.com/catalogue/") 
    page.get_by_role("link", name="Details").click()
    page.get_by_role("link", name="Delete").click()
    page.get_by_role("button", name="Delete car").click()

def test_no_cars(page: Page):
    page.goto("https://car-collection-app.onrender.com/catalogue/")
    expect(page.get_by_text("No cars yet")).to_be_visible()

def test_profile_delete(page: Page):
    page.goto("https://car-collection-app.onrender.com/profile/details/")
    page.get_by_role("link", name="Delete").click(timeout=3000)
    expect(page.get_by_text("Are you sure you want to delete your profile?")).to_be_visible()
    page.get_by_role("button", name="Yes").click()

def test_no_profile(page: Page):
    page.goto("https://car-collection-app.onrender.com/")
    expect(page.get_by_text("Create Profile")).to_be_visible()