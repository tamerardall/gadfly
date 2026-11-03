# gadfly — Tasarım Spec'i

Tarih: 2026-11-03

## Amaç
Yayın öncesi bir içerik taslağı (blog yazısı, LinkedIn postu) verildiğinde, okuyucuların gelebilecek itirazlarını, teknik açıkları ve zayıf noktaları önceden bulup her biri için somut bir düzeltme aksiyonu öneren bir Claude Code skill'i.

Motivasyon: Rust blog yazısında okuyucular "C++'ı çok ilkel kullanmışsın" diye eleştirdi. Bu tür eleştiriler yayından önce görülmeli.

## Başarı Ölçütleri
- Rust/C++ yazısı gibi bir taslakta, gerçekte gelen eleştiri türleri (rakip teknolojinin adil temsil edilmemesi gibi) raporda çıkıyor.
- Her itirazın ciddiyeti, kanıt türü ve önerilen aksiyonu dolu.
- Gerçek tartışmalarla desteklenen itirazlar ile yalnızca simülasyondan gelenler ayrı işaretli.

## Kapsam Dışı
Otomatik yeniden yazma, web arayüzü, geçmiş eleştirilerin kalıcı depolanması, ayrı CLI/SDK uygulaması.

## Yapı
```
gadfly/
  SKILL.md              # akış ve orkestrasyon talimatları
  personas/*.md         # her persona için bir prompt dosyası
  report-template.md    # çıktı formatı
```

## Akış
1. **Girdi:** taslak (dosya yolu ya da yapıştırılmış metin) + isteğe bağlı bağlam (hedef kitle, platform). Taslak birkaç cümleden kısaysa kullanıcıya sorulur.
2. **Konu çıkarımı:** ana iddialar, karşılaştırmalar ve teknik iddialar listelenir.
3. **Araştırma subagent'ı:** HN, Reddit ve forumlarda benzer konulardaki yazılara gelen gerçek eleştirileri arar. Kaynak linkli özet döner.
4. **Persona subagent'ları (paralel):** her biri taslağı ve araştırma özetini okuyup kendi açısından itiraz üretir. Başlangıç personaları:
   - Rakip teknoloji uzmanı (ör. C++ uzmanı)
   - Teknik doğruluk denetçisi
   - Şüpheci okuyucu
   - Yeni başlayan
   - "Bu zaten biliniyor" diyen kıdemli
5. **Birleştirme:** tekrarlar elenir. Her itiraz için ciddiyet (yüksek/orta/düşük), kanıt (kaynak linki veya "simülasyon") ve aksiyon (metni düzelt / kaynak ekle / kapsamı daralt / önceden ele al).
6. **Rapor:** `report-template.md` formatında, ciddiyete göre sıralı.

## Hata Yönetimi
- Web araştırması başarısızsa rapor "yalnızca simülasyon" uyarısıyla devam eder.
- Bir persona boş ya da hatalı dönerse raporda belirtilir ve atlanır.

## Doğrulama
- Gerçek Rust/C++ taslağıyla çalıştır, "C++ ilkel kullanım" itirazının çıkıp çıkmadığına bak.
- Web erişimi kapalıyken uyarılı düşüşü doğrula.
- Yeni oturumda skill tetiklenir ve persona subagent'ları paralel çalışır.

## Marka
- Ad: **Gadfly** (Sokrates'in kendine verdiği ad; uyuşuk ata iğne batıran at sineği). Slogan: "Sting your idea before the internet does."
- Renk paleti ve fontlar tamerardal-com sitesinden alındı (pirinç #D4A84A, demir/petrol #24575A / #7DB6AE, taş kâğıdı ve çelik grisi; Big Shoulders, Source Serif 4, IBM Plex Mono).
- Kimlik, renkler, ses tonu ve logo kuralları: `docs/brand-guidelines.md`. Token'lar: `assets/design-tokens.*`.
- README'de animasyonlu SVG görseller kullanılır (`assets/hero.svg`, `flow.svg`, `report-preview.svg`).

## Sonraki Sürüm (v2): Teknik proje ve fikirler
v1 yalnızca yayın öncesi içeriği kapsar. v2 aynı çekirdeği teknik fikirlere genişletir:
- `personas/technical/` altında yeni personalar: mimari eleştirmen, güvenlik, ölçeklenebilirlik, "bu zaten X ile çözülmüş" diyen kıdemli.
- Araştırma kaynağına GitHub issue'ları ve rakip/benzer projeler eklenir.
- Girdi türüne (içerik / teknik fikir) göre persona seti otomatik seçilir.
- v1'de persona dosyaları `personas/content/` altına konur; v2 yeni dosya eklemekten ibaret olur, çekirdek akış değişmez.
