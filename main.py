import cli.onionshare_cli as cli



new_onion = cli.OnionShareCli()
new_onion.createOnion(mode="receive")
new_onion.receive()
