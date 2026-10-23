# 良友 IPTV 台标与 EPG 库 · IPTV

[← 返回良友资源中心](https://maddestalistar.github.io/LiangYou-ResourceHub/) · 首版 2026-10-23

围绕 **频道别名标准化 → M3U 标准属性 → XMLTV 节目指南 ID 对照**，优先提供可维护的基础数据与本地验证脚本，不发布未经授权的直播源与节目指南。

## JSON 资源入口

**[获取统一 JSON 资源目录](https://raw.githubusercontent.com/MaddestAlistar/IPTV/main/index.json)**

`index.json` 包含当前所有 18 个频道的标准名称/别名、XMLTV 演示对应关系及 M3U/XMLTV/台标的文件 URL。它是**频道信息索引**，不是能直接播放的 IPTV 节目源，也不是实时 EPG；真实节目单需合法来源接入。

## 首版完成内容

- [18 个央视基础频道名称与常见别名](data/channel-aliases.csv)：覆盖 CCTV-1—17、CCTV-5+；这只是**名称与别名**，不意味着已接入频道播放源。
- [M3U 频道名称修正脚本](scripts/normalize_m3u.py)：为已有合法 M3U 播放列表统一 `tvg-name` 和展示名称，保留原始 `tvg-id` 和播放 URL，不擅自替换 EPG 频道 ID。
- [EPG 映射检查脚本](scripts/check_epg.py)：读取用户已有 XMLTV 与自己配置的 `epg-map.csv`，输出缺失和未对应的频道。
- [两枚自制演示台标](logos/demo-news.svg)、[演示电影台标](logos/demo-movies.svg)，以及 [样例 M3U](examples/demo.m3u) / [XMLTV](examples/demo.xml)。

## 使用（只处理自己有权使用的列表）

```bash
python3 scripts/normalize_m3u.py examples/demo.m3u examples/demo-normalized.m3u
python3 scripts/check_epg.py examples/demo.xml data/epg-map.csv
python3 -m unittest discover -s tests
```

需要 Python 3 标准库，无第三方依赖。

**注意**：`examples/demo.m3u` 包含 `example.invalid` 演示链接，**不可播放**；`examples/demo.xml` 仅为演示结构，并非真实节目排期；`epg-map.csv` 中的演示 ID 不能作为官方频道 EPG ID 使用。请从合法、稳定的真实 XMLTV 来源人工核对映射。真实台标商标和台标图片有版权，本库不冒用官方台标。

目前没有可长期保证的官方 XMLTV 频道 ID 或持续更新 EPG 源，也**不将演示数据冒充现成直播服务**。
