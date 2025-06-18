# features/environment.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
#import allure_behave
from allure_commons.types import AttachmentType
import allure



def before_all(context):
    # Setup logs, test data, or global configs here if needed
    print("===> Starting test execution")
    #context.allure_adapter = allure_behave.AllureFormatter
    #context.failed_scenarios = set()
    # Clear previous failures at the beginning
    # Clear old rerun file
    with open("rerun.txt", "w"): pass
    context.failed_scenarios = set()


# features/environment.py

def before_scenario(context, scenario):
    # Setup browser before each scenario
    print(f"\n[Before Scenario] Starting: {scenario.name}")
    # if not hasattr(context, 'retry_map'):
    #     context.retry_map = {}
    # context.retry_map[scenario.name] = context.retry_map.get(scenario.name, 0)    
    options = Options()
    options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)    

def after_scenario(context, scenario):    

    # retries = context.retry_map.get(scenario.name, 0)

    if scenario.status == "failed":
        context.failed_scenarios.add(str(scenario.location))


        # with open("rerun.txt", "a") as rerun_file:
        #     rerun_file.write(scenario.location + "\n")
        # context.retry_map[scenario.name] += 1
        # scenario.mark_skipped()
        # scenario._should_retry = True  # Mark for retry
    # else:
    #     scenario._should_retry = False
    
        safe_name = "".join(x for x in scenario.name if x.isalnum() or x in (" ", "_")).rstrip()
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{safe_name}.png")

        success = context.driver.save_screenshot(screenshot_path)
        # allure.attach(
        #             screenshot_path,
        #             #name="screenshot",
        #             attachment_type=AttachmentType.PNG)
        if success:
            print(f"📸 Screenshot saved: {screenshot_path}")
        else:
            print("❌ Screenshot failed to save.")

    context.driver.quit()

# features/environment.py


# def after_step(context, step):
#     if step.status == "failed":
#         allure.attach(
#             context.driver.get_screenshot_as_png(),
#             name="screenshot",
#             attachment_type=AttachmentType.PNG
#        )
        

def after_step(context, step):
    if step.status == "failed":
        if hasattr(context, 'driver'):
            try:
                screenshot = context.driver.get_screenshot_as_png()                
                allure.attach(
                    screenshot,
                    name="screenshot",
                    attachment_type=AttachmentType.PNG
                )
            except Exception as e:
                print(f"[ERROR] Failed to take screenshot: {e}")
        else:
            print("[WARNING] WebDriver not found in context.")




# def after_scenario(context, scenario):
#     # Take screenshot on failure
#     if scenario.status == "failed":
#         screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}.png"
#         os.makedirs("screenshots", exist_ok=True)
#         context.driver.save
#         context.driver.save_screenshot(screenshot_path)
#         print(f"📸 Screenshot saved: {screenshot_path}")

#     # Teardown browser
#     context.driver.quit()
#     print(f"[After Scenario] Finished: {scenario.name}")

def after_all(context):
    with open("rerun.txt", "w") as f:
        for loc in sorted(context.failed_scenarios):
            f.write(loc + "\n")

    print("===> All tests finished")
