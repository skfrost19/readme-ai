"""Functions for building and formatting the badges in the README.md file."""

from readmeai.config.settings import AppConfig, GitHost
from readmeai.core import factory, logger
from readmeai.utils import utils

logger = logger.Logger(__name__)


def format_html_badge_block(badges: list) -> str:
    """Formats the SVG icons into HTML <img src=""> tags."""
    badge_lines = []
    total_badges = len(badges)
    if total_badges < 8:
        badges_per_line = total_badges
    else:
        badges_per_line = total_badges // 2 + (total_badges % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, total_badges, badges_per_line):
        line = "\n".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}" />'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        badge_lines.append(line)

    return "\n\n".join(badge_lines)


def build_html_badge_block(svg_icons: dict, dependencies: list) -> str:
    """Returns a list of badges for the project dependencies."""
    badges = [
        svg_icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in svg_icons
    ]
    # Sort badges by hex value (from light to dark color)
    badges.sort(key=lambda b: int(b[1], 16) if b[1] else 0, reverse=True)
    badges = [badge[0] for badge in badges]
    return format_html_badge_block(badges)


def badge_template(conf: AppConfig) -> str:
    """Return markdown template for badges"""
    if conf.git.source == GitHost.LOCAL.value:
        return conf.md.badges_offline
    else:
        return conf.md.badges_shieldsio


def shieldsio_icons(conf: AppConfig, packages: list, full_name: str):
    """
    Generates badges for the README using shieldsio icons, referencing the
    repository - https://github.com/Aveek-Saha/GitHub-Profile-Badges.
    """
    resource_path = utils.get_resource_path(
        __package__, conf.files.shieldsio_icons
    )
    shieldsio_dict = factory.FileHandler().read(resource_path)

    md_template = badge_template(conf)
    shieldsio_icons = md_template.format(
        conf.md.align,
        build_html_badge_block(shieldsio_dict, packages).format(
            conf.md.badges_style
        ),
        full_name,
        conf.md.badges_style,
    )
    shieldsio_icons = (
        utils.remove_substring(shieldsio_icons)
        if "invalid" in full_name.lower()
        else shieldsio_icons
    )
    return shieldsio_icons


def skill_icons(conf: AppConfig, dependencies: list) -> str:
    """
    Generates badges for the README using skill icons, from the
    repository - https://github.com/tandpfun/skill-icons.
    """
    conf.md.header = (
        "<!--README-AI.md file generated by @eli64s/readme-ai-->\n"
    )
    resource_path = utils.get_resource_path(
        __package__, conf.files.skill_icons
    )
    skill_icons_dict = factory.FileHandler().read(resource_path)

    filtered_icons = [
        icon
        for icon in skill_icons_dict["icons"]["names"]
        if icon in dependencies
    ]
    filtered_icons.extend(["md", "github", "git"])
    icon_names = ",".join(filtered_icons)
    # per_line = (len(filtered_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"
    skill_icons = skill_icons_dict["url"]["base_url"] + icon_names

    if conf.md.badges_style == "skills-light":
        skill_icons = f"{skill_icons}&theme=light"

    return conf.md.badges_skills.format(
        conf.md.align,
        conf.md.image,
        conf.git.name.upper(),
        conf.prompts.slogan,
        conf.md.align,
        skill_icons,
    )
