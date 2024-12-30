import yaml
import os

# Define the path to the configuration yaml file
CONFIG_PATH = os.path.join(os.path.dirname(__file__), './config.yaml')

# Load the configuration from the YAML file once
with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)

API_BASE_URL = config['api']['base_url']
BROKER_ID = config['api']['broker_id']

# map the configuration values to variables
SEND_EMAIL = config['email']['send_address']
READ_EMAIL = config['email']['read_address']
TENANT = config['email']['tenant_id']
EMAIL_APP = config['email']['app_id']
APP_SECRET = config['email']['app_secret']
SUBJECT = config['email']['subject']

ATTACHMENTS_SAVE_DIR = config['paths']['attachments_save_dir']
DATABASE_PATH = config['paths']['database_path']
ETK_BOT_PROCESS_DIR = config['paths']['Electoneek_process_dir']
SCREENSHOTS_DIR = config['paths']['screenshots_dir']
REFERRAL_FILE_STORE_DIR = config['paths']['referral_file_store_dir']
MAIL_ZIP_FILES = config['paths']['mail_zip_files']

IQ2HEALTH_GENERATED_CENSUS_DIR = config['iq2health']['generated_census_dir']
IQ2HEALTH_TEMPLATES_DIR = config['iq2health']['template_dir']

AURA_GENERATED_CENSUS_DIR = config['aura']['generated_census_dir']

ORIENT_EMIAL = config['orient']['email']
ORIENT_PASSWORD = config['orient']['password']
ORIENT_QUOTATION_DIR = config['orient']['quotation_download_dir']

RAK_EMIAL = config['rak']['email']
RAK_PASSWORD = config['rak']['password']
RAK_QUOTATION_DIR = config['rak']['quotation_download_dir']

TAKAFUL_EMAIL = config['takaful']['email']
TAKAFUL_PASSWORD = config['takaful']['password']
TAKAFUL_QUOTATION_DIR = config['takaful']['quotation_download_dir']

NLG_USERNAME = config['NLG']['username']
NLG_PASSWORD = config['NLG']['password']
NLG_GENERATED_CENSUS_DIR = config['NLG']['generated_census_dir']
NLG_TEMPLATES_DIR = config['NLG']['templates_dir']
NLG_QUOTATION_DIR = config['NLG']['quotation_download_dir']

SUKOON_EMAIL = config['sukoon']['email']
SUKOON_PASSWORD = config['sukoon']['password']
SUKOON_GENERATED_CENSUS_DIR = config['sukoon']['generated_census_dir']
SUKOON_TEMPLATES_DIR = config['sukoon']['templates_dir']
SUKOON_QUOTATION_DIR = config['sukoon']['quotation_download_dir']
SUKOON_TEMP_IMG_DIR = config['sukoon']['temp_img_dir']

DNI_EMIAL = config['dni']['email']
DNI_PASSWORD = config['dni']['password']
DNI_QUOTATION_DIR = config['dni']['quotation_download_dir']

QATAR_EMAIL = config['qatar']['email']
QATAR_PASSWORD = config['qatar']['password']
QATAR_QUOTATION_DIR = config['qatar']['quotation_download_dir']

COMPARISON_GENERATED_DIR = config['comparison']['generated_comparison_dir']
COMPARISON_TEMPLATE = config['comparison']['template']

POPPLER_PATH = config['poppler']['path']

TWO_CAPTCHA_API_KEY = config['captcha']['api_key']

IS_HEADLESS = config['modes']['headless']
IS_PARALLEL = config['modes']['parallel']

MIN_SLEEP = config['sleep']['min']
MED_SLEEP = config['sleep']['med']
MAX_SLEEP = config['sleep']['max']

MAX_RETRIES = config['retry']['max_attempts']

MAX_REFERRAL_MINUTES = config['referrals']['max_minutes']
IS_REFERRAL_ACTIVE = config['referrals']['active']