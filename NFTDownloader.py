#!/usr/bin/python

###########################################################################
#
# name          : NFTDownloader.py
#
# purpose       : Download NFT's and metadata
#
# usage         : python NFTDownloader.py
#
# description   :
#
###########################################################################


import json
import os
import requests
import shutil
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def create_dirs( name=None ) :
    assert name is not None, "'name' cannot be 'None'"

    try :
        os.mkdir( name )
    except :
        pass

    try :
        os.mkdir( os.path.join( name, "images" ) )
    except :
        pass

    try :
        os.mkdir( os.path.join( name, "metadata" ) )
    except :
        pass


def get_images( name=None, contract_address=None, total_count=None ) :
    assert name is not None, "'name' cannot be 'None'"
    assert contract_address is not None, "'contract_address' cannot be 'None'"
    assert total_count is not None, "'total_count' cannot be 'None'"
    for i in range( total_count ) :
        if os.path.exists( open( os.path.join( name, "images", "%05u.jpg" % i ), 'wb' ) ) :
            continue
        print( "--> Images: %05u" % i, end="\r" )
        url = f"https://img.x2y2.io/v2/1/{contract_address}/{i}/280/image.jpg"
        response = requests.get( url, stream=True, headers=headers )
        with open( os.path.join( name, "images", "%05u.jpg" % i ), 'wb' ) as f :
            shutil.copyfileobj( response.raw, f )
        time.sleep( 1 )
    print( f"--> Image downloading complete for '{name}'" )


def get_metadata( name=None, contract_address=None, alchemy_key=None, total_count=None ) :
    assert name is not None, "'name' cannot be 'None'"
    assert contract_address is not None, "'contract_address' cannot be 'None'"
    assert alchemy_key is not None, "'alchemy_key' cannot be 'None'"
    assert total_count is not None, "'total_count' cannot be 'None'"

    index = 0
    while index < total_count + 100 :
        print( "--> Metadata: %05u" % index, end="\r" )
        url = f"https://eth-mainnet.g.alchemy.com/nft/v2/{alchemy_key}/getNFTsForCollection?contractAddress={contract_address}&withMetadata=true&startToken={index}&limit=100" 
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        json_data = json.loads( response.text )
        with open( os.path.join( name, "metadata", f"{index}.json" ), 'w' ) as f :
            json.dump( json_data, f, indent=2 )
        index += 100
    print( f"--> Metadata downloading complete for '{name}'" )


if __name__ == "__main__" :
    import optparse
    parser = optparse.OptionParser()
    parser.add_option( "-c", "--config", dest="config", action="store", default="data/config.json", help="Config file", metavar="STRING" )
    ( options, args ) = parser.parse_args()

    config = None
    with open( options.config, 'r' ) as f :
        config = json.load( f )

    alchemy_key = config[ "alchemy_key" ]
    nfts = config[ "nfts" ]
    for nft in nfts :
        print( "--> %s" % nft[ "name" ] )
        create_dirs( nft[ "name" ] )
        args = { "name" : nft[ "name" ], "contract_address" : nft[ "contract_address" ], "total_count" : nft[ "total_count" ] }
        get_images( **args )
        args = { "name" : nft[ "name" ], "contract_address" : nft[ "contract_address" ], "alchemy_key" : alchemy_key, "total_count" : nft[ "total_count" ] }
        get_metadata( **args )
