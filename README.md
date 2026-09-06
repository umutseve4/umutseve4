<div align="center">

<img width="100%" alt="ZİFT — evidence over adjectives, nothing quietly fixed" src="https://umutseve4.github.io/cover/zift-banner.svg">

<br>

![33 public repositories](https://img.shields.io/badge/33-public%20repositories-0B0B0B?style=flat-square&labelColor=0B0B0B)
![12 live surfaces](https://img.shields.io/badge/12-live%20surfaces-0B0B0B?style=flat-square&labelColor=0B0B0B)
![16 stars](https://img.shields.io/badge/16-stars-0B0B0B?style=flat-square&labelColor=0B0B0B)

</div>

---

Bir iddia yazmadan önce onu ölçen testi yazıyorum.
Ekranda gördüğünüz her şey ya tarayıcıda açılıyor ya bir komutla çalışıyor.
Açılmayan, çalışmayan, ölçülmeyen şey bu sayfada yer almıyor.

**Umut Sever** — Bursa Uludağ Üniversitesi, Ekonometri (dersler 28 Eylül 2026'da başlıyor).

---

## ▸ 30 saniyede ne yapabilirsin

Kurulum yok, klonlama yok. Aşağıdaki bağlantılar şu anda canlı:

| Aç | Ne görürsün | Süre |
| --- | --- | --- |
| [Cosmic Econometric Observatory](https://umutseve4.github.io/cosmic-econometric-observatory/) | Ekonometri müfredatının 147 düğüm / 146 kenarlık bilgi evreni; ders seçince ön koşul zinciri aydınlanır | ~60 sn |
| [EkoDiff](https://umutseve4.github.io/ekodiff/) | İki müfredat sürümünü yan yana koyar, hangi dersin eklendiğini/kalktığını satır satır gösterir | ~40 sn |
| [Tercih Atlası](https://umutseve4.github.io/tercih-atlasi/) | EA/SAY alanları için açıklanabilir tercih haritası — her skorun altında nedeni yazıyor | ~45 sn |
| [Uludağ Kampüs Turu](https://umutseve4.github.io/uludag-campus-tour-webgl/) | Görükle kampüsünde tek dosyalık sinematik yürüyüş, WebGL | ~90 sn |
| [Çanakkale 1915](https://umutseve4.github.io/canakkale-1915-webgl/) | Prosedürel deniz, sis ve ışık; hiçbir varlık dosyası indirilmez | ~90 sn |
| [PulseGrid 3D](https://umutseve4.github.io/pulsegrid-3d/) | Veri hattı sağlığını şehir olarak gösteren canlı görselleştirme | ~60 sn |
| [Gallipoli 1915](https://umutseve4.github.io/gallipoli-1915-webgl/) | Aynı sahnenin İngilizce anlatımlı sürümü | ~90 sn |
| [SEVER/05 — portföy](https://umutseve4.github.io/) | Tüm yüzeylerin tek sayfalık girişi | ~20 sn |

Üçüncü bir adım yok. Beğenmezsen sekmeyi kapat.

## ▸ Yerelde çalıştır

```bash
git clone https://github.com/umutseve4/econ-lakehouse.git
cd econ-lakehouse
make setup && make run
```

Çıktı: bronze → silver → gold katmanları, her katman için satır sayısı ve kalite kapısı sonucu. Veri kaynağı repoya işlenmiş sentetik bir fixture'dır; ağ gerektirmez, iki çalıştırma aynı sonucu verir.

## ▸ Ne üzerine çalışıyorum

| Alan | Repo | Sorduğu soru |
| --- | --- | --- |
| Veri mimarisi | [econ-lakehouse](https://github.com/umutseve4/econ-lakehouse) | Bir makro seri katmandan katmana geçerken ne kaybeder? |
| Kanıt & sürüm | [RevisionLedger](https://github.com/umutseve4/RevisionLedger) | 2023'te açıklanan rakam, bugünkü revizyondan önce neydi? |
| Belge erişimi | [tcmb-policy-rag-pipeline](https://github.com/umutseve4/tcmb-policy-rag-pipeline) | PPK metnindeki bir cümleyi kaynağına kadar takip edebilir miyim? |
| Ölçüm | [enflasyonum](https://github.com/umutseve4/enflasyonum) | Kendi sepetimle hesaplanan Laspeyres endeksi TÜİK'ten ne kadar sapıyor? |
| Dayanıklılık | [data-reliability-lab](https://github.com/umutseve4/data-reliability-lab) | Hat bozulduğunda kayıt karantinaya mı düşüyor, sessizce mi geçiyor? |
| Öğrenci araçları | [eko-rasathane](https://github.com/umutseve4/eko-rasathane) · [ekodiff](https://github.com/umutseve4/ekodiff) | Müfredat değiştiğinde öğrenci bunu nereden öğrenecek? |
| Gerçek zamanlı grafik | [canakkale-1915-webgl](https://github.com/umutseve4/canakkale-1915-webgl) · [neon-lunapark-webgl](https://github.com/umutseve4/neon-lunapark-webgl) | Tek dosya, sıfır varlık, kaç kare taşır? |

## ▸ Ölçüm

| Ne | Değer | Nasıl doğrulanır |
| --- | --- | --- |
| Herkese açık repo | 33 | GitHub API `/users/umutseve4/repos` |
| Yayında olan Pages yüzeyi | 12 | Aynı yanıtta `has_pages` |
| Yıldız (herkese açık) | 16 | Aynı yanıtta `stargazers_count` toplamı |
| Müfredat kaydı — Cosmic | 144 ders, 147 düğüm, 146 kenar | Depodaki dataset ve doğrulama testi |
| Marka varlığı — ZİFT | 1 vektör master, 17 raster, 1 favicon | CI iş akışı her push'ta yeniden üretir |

Bu tablodaki hiçbir sayı elle yazılmadı; her biri bir uç noktadan ya da bir testten okundu.

## ▸ Nasıl yapıldı

Tek renk kuralı var: `#FF4D4F`. Vurgu bir kere kullanılır, iki kere kullanılırsa vurgu olmaktan çıkar.
Görsel varlıklar depoya elle atılmaz; ZİFT markasının 18 çıktısı tek bir vektör kaynaktan CI tarafından üretilir.
Her repo, kendi CI'ı yeşilken yayına girer — kırmızı bir kapıyı "sonra bakarım" diye geçmiyorum.

### Sınırlar

- `econ-lakehouse` gerçek TÜİK/TCMB akışına bağlı değil; işlenmiş sentetik bir fixture üzerinde çalışır ve tazelik feragati **5 Ekim 2026**'da sona erer.
- WebGL sahneleri masaüstü tarayıcıda ölçüldü; düşük güçlü mobil cihazlarda kare hızı garanti edilmiyor.
- Yukarıdaki yıldız ve repo sayıları yalnızca herkese açık depoları kapsar.
- Ekonometri lisansım henüz başlamadı; buradaki ekonometrik iş öğrenme sürecinin çıktısıdır, akademik yayın değildir.

---

<div align="center">

Kod MIT, metin CC BY 4.0 · **evidence over adjectives, nothing quietly fixed**

</div>
