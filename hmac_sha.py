def sign_request():
    from hashlib import sha1
    import hmac

    # key = CONSUMER_SECRET& #If you dont have a token yet
    #key = "swbs75i58ztiplvmti18epp52q83e2v3&" 
    key = "testKey"

    # The Base String as specified here: 
    #raw = "MQTT&mqtt%3A%2F%2Fmqtt.magellanic-clouds.com&oauth_consumer_key%3Delin2015.Project1%26oauth_nonce%3D1439788188%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1439788188%26oauth_version%3D1.0" # as specified by oauth
    raw = "testing"

    hashed = hmac.new(key, raw, sha1)

    # The signature
    print(hashed.digest().encode("base64").rstrip('\n'))
    return hashed.digest().encode("base64").rstrip('\n')

sign_request()
