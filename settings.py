import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

project_dir = os.path.join(os.path.dirname(__file__))
DEMOGRAPHICS_PATH = os.path.join(project_dir, "data", "raw", "demographic_info.csv")
AMBIGUITY_PATH = os.path.join(project_dir, "data", "raw", "ambiguity_dataset.csv.gz")
AMBIGUITY_CLUSTER = os.environ.get("AMBIGUITY_CLUSTER")
EMBEDDINGS_PATH = os.path.join(project_dir, "data", "interim", "glove-twitter-200-ambiguity.bin")
EMBEDDINGS_CLUSTER = os.environ.get("EMBEDDINGS_CLUSTER")
AMBIGUITY_VARIATION = os.path.join(project_dir, "data", "interim", "ambiguity_variation.csv.gz")
EMOJI_IMGS = os.path.join(project_dir, "data", "external", "emoji_imgs")
EMOJI_IMGS_CLUSTER = os.environ.get("EMOJI_IMGS_CLUSTER")
EMOJI_CATEGORIZED = os.path.join(project_dir, "data", "external", "emoji_categories.pkl")
TWITTER_TOKEN = os.environ.get("TWITTER_TOKEN")
