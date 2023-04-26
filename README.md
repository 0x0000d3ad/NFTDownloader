# NFTDownloader
 Download images and metadata from your favorite NFT projects!

# Installation
 Dependencies include the 'requests' module.  Install this using pip:

 `pip install requirements`

 or use requirements.txt:

 `pip -r requirements.txt`

# Contents 
 This repo contains the following contents:

 1. `NFTDownloader.py` - Script that downloads images and metadata for NFT projects, specified in `./data/config.json`.
 2. `data/config.json` - Configuration file for NFT data and Alchemy API key.

# Running NFTDownloader

 The following steps will get you started running NFTDownloader:

 1. [Install dependencies](./README.md#Installation)
 2. Get an Alchemy API key
 3. Enter information into [the config file](./data/config.json)
 4. Run the script

## Install Dependencies
 You should have Python 3 installed.  Python 3.11.3 was used to test the script.  See [Installation](./README.md#Installation) above for installing dependencies.

## Get an Alchemy API Key
 You need an API key for alchemy to run this code.  See their [Quickstart Guide](https://docs.alchemy.com/docs/alchemy-quickstart-guide) for instructions on setting up an API key and getting familiar with the service.  To run this code, all you need is the API key.

## Enter Information the Config File
 We have started a config file for you [here](./data/config.json).  You need to set the following information:

 1. Your Alchemy API Key - set the `alchemy_key` in your config file
 2. Set NFT data in the config file.  The the data is in a list, so that you can download multiple NFT projects.  Each entry in the list has the following properties:
 - `name` - Text name of the project
 - `contract_address` - Contract address
 - `total_count` - Total amount of existing tokens, including burned tokens.  Note 'total_supply' is commonly used to refer to the amount *less* burned tokens.

 To get you started, data for 'Cryptoadz' and 'Doodles' is supplied.

## Running the Script
 To run the script, navigate to the directory and run the following command:

 `python NFTDownloader.py -c data/config.json`

 If you chose a different name other than 'config.json' for your config file, then include that name in the line above, instead.

 The script will create directories for each project you specified.  Contained in each directory are subdirectories for the images and metadata.

# Tips Accepted
 If you used the script, feel free to tip!

 0x2E4fC8b95eCCf331955b93dE349C12B6f59BD76B
