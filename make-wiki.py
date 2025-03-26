import argparse
import datetime
import re
from pathlib import Path

from tiddlywiki_parser import readers, tiddlywiki

DEFAULT_PRIVATE = True
PRIVATE_TAGS = ["gm", "private"]
PUBLIC_TAGS = ["player", "public"]


# def fix_tags(tags):
#     matches = re.findall(r"\[\[(.*?)\]\]", tags)  # Extract contents inside [[ ]]
#     cleaned_text = re.sub(r"\[\[.*?\]\]", "", tags).strip()
#     return matches + cleaned_text.split()


def extract_from_private(tiddler):
    pattern = rf"@@\.({'|'.join(map(re.escape, PUBLIC_TAGS))})[\s\S]*?@@"
    matches = [match.group(0) for match in re.finditer(pattern, tiddler.text)]
    if matches:
        tiddler.text = "\n\n".join(matches)
        print(tiddler.text)
    else:
        return tiddler.title


def clean_public(tiddler):
    pattern = rf"@@\.({'|'.join(map(re.escape, PRIVATE_TAGS))})[\s\S]*?@@"
    print(tiddler.text)
    tiddler.text = re.sub(pattern, "", tiddler.text).strip()
    print(tiddler.text)


def clean_wiki(wiki):
    delete_list = []
    for tiddler in wiki.tiddlers:
        if tiddler.title == "Welcome":
            tiddler["version"] = "Player's"
        elif tiddler.title == "generation_timestamp":
            now = datetime.datetime.now()
            tiddler["timestamp"] = now.isoformat()

        private = False or DEFAULT_PRIVATE
        for tag in tiddler.tags:
            if tag in PUBLIC_TAGS:
                private = False
            if tag in PRIVATE_TAGS:
                private = True
                break
        if private:
            to_delete_title = extract_from_private(tiddler)
            if to_delete_title:
                delete_list.append(to_delete_title)
        else:
            clean_public(tiddler)
    return wiki, delete_list


# def remove_github(content):
#     """
#     Remove the github save values, so they can't use it to find the GM version.
#     No reason to tempt them.
#     """
#     # Define the regex pattern (handling multiline cases)
#     pattern = re.compile(
#         r'<div created="\d+" modified="\d+" title="\$:/GitHub/[\w-]+">\s*'
#         r"<pre>[^<]*</pre>\s*</div>",
#         re.DOTALL,
#     )

#     # print(re.findall(pattern, content))
#     # return content

#     # Remove matching patterns
#     return re.sub(pattern, "", content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="The tiddlywiki src.  May be a path or url.")
    parser.add_argument("dst", help="The tiddlywiki dest.  Must be a file path.")
    args = parser.parse_args()

    content = readers.read(args.src)
    wiki = tiddlywiki.TiddlyWiki(content)
    github_delete_list = [t.title for t in wiki.system_tiddlers if "GitHub" in t.title]
    wiki, delete_list = clean_wiki(wiki)
    delete_list += github_delete_list
    print(len(wiki.tiddlers))
    new_wiki = wiki.remake(delete_list)
    f = Path(args.dst)
    f.write_text(new_wiki, encoding="utf8")
    print(f"Player wiki written to {args.dst}")


if __name__ == "__main__":
    main()
