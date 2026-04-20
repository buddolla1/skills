from __future__ import annotations

import zipfile
from pathlib import Path
from xml.sax.saxutils import escape


OUT_FILE = Path("skills-overview.pptx")

EMU_PER_INCH = 914400
SLIDE_W = 13.333 * EMU_PER_INCH
SLIDE_H = 7.5 * EMU_PER_INCH

NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"


def emu(value: float) -> int:
    return int(round(value * EMU_PER_INCH))


def xml_escape(text: str) -> str:
    return escape(text, {"\n": "&#10;"})


def tx_box(shape_id: int, name: str, x: int, y: int, cx: int, cy: int, paragraphs: list[dict]) -> str:
    paras: list[str] = []
    for idx, para in enumerate(paragraphs):
        text = xml_escape(para["text"])
        size = para.get("size", 1800)
        bold = "1" if para.get("bold", False) else "0"
        color = para.get("color", "1F2937")
        align = para.get("align")
        para_props = []
        if align:
            para_props.append(f'a:algn="{align}"')
        para_props_s = " ".join(para_props)
        paras.append(
            f"""
            <a:p>
              <a:pPr {para_props_s}/>
              <a:r>
                <a:rPr lang="en-US" sz="{size}" b="{bold}" dirty="0">
                  <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
                  <a:latin typeface="Aptos"/>
                </a:rPr>
                <a:t>{text}</a:t>
              </a:r>
              <a:endParaRPr lang="en-US" sz="{size}" b="{bold}">
                <a:solidFill><a:srgbClr val="{color}"/></a:solidFill>
                <a:latin typeface="Aptos"/>
              </a:endParaRPr>
            </a:p>
            """.strip()
        )
        if idx != len(paragraphs) - 1:
            paras.append(
                """
                <a:p>
                  <a:r><a:t></a:t></a:r>
                </a:p>
                """.strip()
            )

    return f"""
    <p:sp>
      <p:nvSpPr>
        <p:cNvPr id="{shape_id}" name="{xml_escape(name)}"/>
        <p:cNvSpPr txBox="1"/>
        <p:nvPr/>
      </p:nvSpPr>
      <p:spPr>
        <a:xfrm>
          <a:off x="{x}" y="{y}"/>
          <a:ext cx="{cx}" cy="{cy}"/>
        </a:xfrm>
        <a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
        <a:noFill/>
      </p:spPr>
      <p:txBody>
        <a:bodyPr wrap="square" rtlCol="0">
          <a:spAutoFit/>
        </a:bodyPr>
        <a:lstStyle/>
        {''.join(paras)}
      </p:txBody>
    </p:sp>
    """.strip()


def slide_xml(title: str, body: str | None = None, bullets: list[str] | None = None, subtitle: str | None = None, footer: str | None = None) -> str:
    elements: list[str] = []
    title_top = emu(0.62)
    title_left = emu(0.70)
    title_width = emu(11.8)
    title_height = emu(0.8)
    body_top = emu(1.55)
    body_left = emu(0.88)
    body_width = emu(11.55)
    body_height = emu(5.3)

    elements.append(
        tx_box(
            1,
            "Title 1",
            title_left,
            title_top,
            title_width,
            title_height,
            [{"text": title, "size": 3000, "bold": True, "color": "0F766E"}],
        )
    )

    if subtitle:
        elements.append(
            tx_box(
                2,
                "Subtitle 1",
                title_left,
                emu(1.25),
                emu(11.2),
                emu(0.45),
                [{"text": subtitle, "size": 1550, "color": "5B6472"}],
            )
        )

    if body:
        elements.append(
            tx_box(
                3,
                "Body 1",
                body_left,
                body_top,
                body_width,
                body_height,
                [{"text": body, "size": 1800, "color": "1F2937"}],
            )
        )

    if bullets:
        bullet_paras = [{"text": f"• {item}", "size": 1850, "color": "1F2937"} for item in bullets]
        elements.append(
            tx_box(
                4,
                "Bullets 1",
                body_left,
                body_top,
                body_width,
                body_height,
                bullet_paras,
            )
        )

    if footer:
        elements.append(
            tx_box(
                5,
                "Footer 1",
                emu(0.88),
                emu(6.72),
                emu(11.2),
                emu(0.28),
                [{"text": footer, "size": 1200, "color": "5B6472"}],
            )
        )

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld>
    <p:bg>
      <p:bgPr>
        <a:solidFill><a:srgbClr val="F4F1EB"/></a:solidFill>
        <a:effectLst/>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="0" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      {''.join(elements)}
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr>
    <a:masterClrMapping/>
  </p:clrMapOvr>
</p:sld>
"""


def blank_sp_tree() -> str:
    return f"""
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
    """.strip()


def theme_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">
  <a:themeElements>
    <a:clrScheme name="Office">
      <a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>
      <a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1F2937"/></a:dk2>
      <a:lt2><a:srgbClr val="F4F1EB"/></a:lt2>
      <a:accent1><a:srgbClr val="0F766E"/></a:accent1>
      <a:accent2><a:srgbClr val="134E4A"/></a:accent2>
      <a:accent3><a:srgbClr val="F59E0B"/></a:accent3>
      <a:accent4><a:srgbClr val="2563EB"/></a:accent4>
      <a:accent5><a:srgbClr val="7C3AED"/></a:accent5>
      <a:accent6><a:srgbClr val="DC2626"/></a:accent6>
      <a:hlink><a:srgbClr val="2563EB"/></a:hlink>
      <a:folHlink><a:srgbClr val="7C3AED"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="Office">
      <a:majorFont>
        <a:latin typeface="Aptos Display"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:majorFont>
      <a:minorFont>
        <a:latin typeface="Aptos"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="Office">
      <a:fillStyleLst>
        <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
        <a:gradFill flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:schemeClr val="phClr"/></a:gs>
            <a:gs pos="100000"><a:schemeClr val="phClr"/></a:gs>
          </a:gsLst>
          <a:lin ang="16200000" scaled="1"/>
        </a:gradFill>
        <a:gradFill flip="none" rotWithShape="1">
          <a:gsLst>
            <a:gs pos="0"><a:schemeClr val="phClr"/></a:gs>
            <a:gs pos="100000"><a:schemeClr val="phClr"/></a:gs>
          </a:gsLst>
          <a:lin ang="16200000" scaled="1"/>
        </a:gradFill>
      </a:fillStyleLst>
      <a:lnStyleLst>
        <a:ln w="9525" cap="flat" cmpd="sng" algn="ctr">
          <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
          <a:prstDash val="solid"/>
          <a:miter lim="800000"/>
        </a:ln>
        <a:ln w="25400" cap="flat" cmpd="sng" algn="ctr">
          <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
          <a:prstDash val="solid"/>
          <a:miter lim="800000"/>
        </a:ln>
        <a:ln w="38100" cap="flat" cmpd="sng" algn="ctr">
          <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
          <a:prstDash val="solid"/>
          <a:miter lim="800000"/>
        </a:ln>
      </a:lnStyleLst>
      <a:effectStyleLst>
        <a:effectStyle><a:effectLst/></a:effectStyle>
        <a:effectStyle><a:effectLst/></a:effectStyle>
        <a:effectStyle><a:effectLst/></a:effectStyle>
      </a:effectStyleLst>
      <a:bgFillStyleLst>
        <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
        <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
        <a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
      </a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>
"""


def master_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld>
    {blank_sp_tree()}
  </p:cSld>
  <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>
  <p:sldLayoutIdLst>
    <p:sldLayoutId id="2147483649" r:id="rId1"/>
  </p:sldLayoutIdLst>
  <p:txStyles>
    <p:titleStyle/>
    <p:bodyStyle/>
    <p:otherStyle/>
  </p:txStyles>
</p:sldMaster>
"""


def layout_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" type="blank" preserve="1">
  <p:cSld>
    {blank_sp_tree()}
  </p:cSld>
  <p:clrMapOvr>
    <a:masterClrMapping/>
  </p:clrMapOvr>
</p:sldLayout>
"""


def presentation_xml(num_slides: int) -> str:
    slide_ids = "\n".join(
        f'    <p:sldId id="{256 + i}" r:id="rId{2 + i}"/>' for i in range(num_slides)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:sldMasterIdLst>
    <p:sldMasterId id="2147483648" r:id="rId1"/>
  </p:sldMasterIdLst>
  <p:sldIdLst>
{slide_ids}
  </p:sldIdLst>
  <p:sldSz cx="{int(SLIDE_W)}" cy="{int(SLIDE_H)}" type="screen16x9"/>
  <p:notesSz cx="685800" cy="914400"/>
</p:presentation>
"""


def presentation_rels(num_slides: int) -> str:
    rels = [
        f'  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>'
    ]
    for i in range(num_slides):
        rels.append(
            f'  <Relationship Id="rId{2 + i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i + 1}.xml"/>'
        )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{NS_PKG_REL}">
{chr(10).join(rels)}
</Relationships>
"""


def root_rels() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{NS_PKG_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>
"""


def content_types(num_slides: int) -> str:
    overrides = [
        '  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>',
        '  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>',
        '  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>',
        '  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>',
    ]
    overrides.extend(
        f'  <Override PartName="/ppt/slides/slide{i + 1}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(num_slides)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="{NS_CT}">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
{chr(10).join(overrides)}
</Types>
"""


def write_pptx(path: Path) -> None:
    slides = [
        slide_xml(
            "Skills Overview",
            subtitle="Agent Skills are a portable, open format for adding specialized capabilities, workflows, and reference material to AI agents on demand.",
            footer="Presentation-ready summary of the Agent Skills format.",
        ),
        slide_xml(
            "What Skills Are",
            body="Each skill is a self-contained directory centered on SKILL.md. The file defines the skill's purpose, when it should activate, and how the agent should execute it.",
            bullets=[
                "Required metadata such as name and description",
                "Instructions that tell an agent how to perform a task",
                "Optional scripts, templates, and reference materials",
            ],
            footer="Core unit: one folder, one purpose.",
        ),
        slide_xml(
            "How Skills Work",
            bullets=[
                "Discovery: the agent loads only the skill name and description.",
                "Activation: when the task matches, the agent loads the full SKILL.md.",
                "Execution: the agent follows the instructions and loads supporting files only when needed.",
            ],
            footer="Progressive disclosure keeps the base context lean.",
        ),
        slide_xml(
            "Why Skills Matter",
            bullets=[
                "Clear intent for both humans and agents",
                "Better reuse across many tasks and agents",
                "Portable files that are easy to version and share",
                "Extensible delivery through code, examples, and references",
                "Consistent execution for complex workflows",
            ],
            footer="Skills turn expert knowledge into reusable capability.",
        ),
        slide_xml(
            "Skills vs Custom Instructions",
            body="Use skills for reusable capabilities. Use custom instructions for project rules, coding conventions, and review preferences.",
            footer="Different tools for different levels of customization.",
        ),
        slide_xml(
            "Specification Highlights",
            bullets=[
                "A skill is a directory containing SKILL.md, with optional scripts/, references/, and assets/ folders.",
                "Key fields include name, description, license, compatibility, metadata, and allowed-tools.",
                "Keep the main SKILL.md concise, load supporting files only when needed, and validate the skill before publishing.",
            ],
            footer="Specification keeps the format portable and predictable.",
        ),
        slide_xml(
            "Scripts and Examples",
            bullets=[
                "Use one-off commands when an existing tool already solves the job well.",
                "Bundle scripts when the workflow is complex enough to benefit from tested, reusable logic.",
                "Avoid interactive prompts; use clear help text, structured output, and safe defaults.",
            ],
            footer="Scripts should be reliable, non-interactive, and agent-friendly.",
        ),
        slide_xml(
            "Examples and Repository Context",
            bullets=[
                "Valid names: pdf-processing, data-analysis, code-review",
                "Invalid names: PDF-Processing, -pdf, pdf--processing",
                "Good description: specific, task-focused, and clear about when to use it",
                "The repository root SKILL.md is the index for available skills.",
            ],
            footer="Use the most specific skill that matches the task.",
        ),
    ]

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types(len(slides)))
        zf.writestr("_rels/.rels", root_rels())
        zf.writestr("ppt/presentation.xml", presentation_xml(len(slides)))
        zf.writestr("ppt/_rels/presentation.xml.rels", presentation_rels(len(slides)))
        zf.writestr("ppt/theme/theme1.xml", theme_xml())
        zf.writestr("ppt/slideMasters/slideMaster1.xml", master_xml())
        zf.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="{NS_PKG_REL}">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>
""")
        zf.writestr("ppt/slideLayouts/slideLayout1.xml", layout_xml())
        for idx, slide in enumerate(slides, start=1):
            zf.writestr(f"ppt/slides/slide{idx}.xml", slide)


if __name__ == "__main__":
    write_pptx(OUT_FILE)
    print(f"Wrote {OUT_FILE}")
