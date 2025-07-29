# ---- in-app functions ----
"""def search_vault(vault_data):  # DEPRACTED: USING PYDOC.PAGER's BUILT IN SEARCH '/' WHEN VIEWING ENTRIES
    print("Type 'exit' to quit.")
    while True:
        query = input("Search> ").strip()
        if query.lower() == "exit":
            break
        keys = list(vault_data.keys())
        matches = process.extract(query, keys, limit=5, score_cutoff=50)

        results = [(match[0], vault_data[match[0]]) for match in matches]
        if results:
            print("Matches:")
            for name, details in results:
                print(f" - {name}: {details}")
        else:
            print("No matches found.")
"""

def add_entry(vault_data):
    website = input('website: ')
    username = input('Username: ')
    password = input('Password: ')
    notes = input('Notes: ')

    if website not in vault_data: # type: ignore
        vault_data[website] = {} # type: ignore
    vault_data[website][username] = {'Password': password, 'Notes': notes} # type: ignore

    return vault_data


def delete_entry(vault_data):
    if not vault_data:
        print('vault is empty!')
        return vault_data

    print('--- DELETE MODE ---')
    print('Current entries:')
    for site, users in vault_data.items():
        for username in users:
            print(f'- {site} {username}')

    target_website = input('\nChoose website (leave blank to exit): ')

    if target_website not in vault_data:
        print('Website not found')
        return vault_data

    target_username = input('Choose username (leave blank to remove all): ')

    confirmation = input(f"Really delete {target_username} for {target_website}? (y/N): ")
    if confirmation.lower() != 'y':
        print("Cancelled")
        return vault_data

    if target_username == "":
        del vault_data[target_website]
        print(f'all entries for: {target_website} have been deleted')
    else:
        if target_username in vault_data[target_website]:
            del vault_data[target_website][target_username]
            print(f"\n{target_username} for {target_website} has been deleted")
        else:
            print('username not found!')

    return vault_data

