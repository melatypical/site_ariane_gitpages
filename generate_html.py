import os
import json
from datetime import datetime

# Permet de générer l'ensemble des pages HTML travaux de chaque GT à partir du fichier JSON

INPUT_JSON = "documents.json"
OUTPUT_DIR = "html_pages"
HTML_TEMPLATE = """<!doctype html>
<html lang="fr-fr">
<head>
    <base href=".">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" sizes="180x180" href="assets/img/logoAriane.jpg">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://getbootstrap.com/docs/5.3/assets/css/docs.css" rel="stylesheet">
    <link rel="stylesheet" href="assets/main.css">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <style>
        .dropdown:hover>.dropdown-menu {{display: block;}}
        .dropdown-submenu {{
            position: relative;
        }}
        .dropdown-submenu:hover>.dropdown-menu {{
            display: block;
        }}
        .dropdown-submenu .dropdown-menu {{
            top: 0;
            left: 100%;
            margin-top: -1px;
        }}
    </style>
</head>
<body>
    <!-- Header consortium -->
    <header class="relative bg-white mb-2 w-100" style="box-shadow: 0 0 10px rgba(143, 0, 6, 0.1);">
        <div class="border-top border-danger"></div>
        <div class="header-content container">
            <div class="header-logos d-flex align-items-center">
                <!--Logo Ariane-->
                <a href="https://cst-ariane.huma-num.fr/" class="me-2">
                    <img src="assets/img/logoAriane.jpg" alt="CST-HN ARIANE logo">
                </a>
                <!--Logo Humanum-->
                <a href="https://www.huma-num.fr/">
                    <img src="assets/img/HN.png" alt="Huma-Num logo">
                </a>
            </div>
            <!--Menu-->
            <nav>
                <ul class="nav">
                    <li class="nav-item dropdown">
                        <a class="nav-link text-gray-400 text-xl transition hover:text-gray-400/75 dropdown-toggle" href="#" id="axesDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Axes
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="axesDropdown">
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle" href="https://consortiumariane.gitpages.huma-num.fr/axe1">Axe 1</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/GT1/GT1.html">Labellisation</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/GT2/GT2.html">Acquisition de données et transcription par ordinateur</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/GT3/GT3.html">Outils et pratiques éditoriales</a></li>
                                </ul>
                            </li>
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle" href="https://consortiumariane.gitpages.huma-num.fr/axe2">Axe 2</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/GT4/GT4.html">Analyse automatique de texte</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/GT5/GT5.html">Métadonnées et modélisation de données</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/GT6/GT6.html">Open French Corpus</a></li>
                                </ul>
                            </li>
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle" href="https://consortiumariane.gitpages.huma-num.fr/axe3">Axe 3</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe3/ethique/ethique.html">Enjeux éthiques</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe3/juridique/juridique.html">Questions juridiques</a></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link text-gray-400 text-xl transition hover:text-gray-400/75 dropdown-toggle" href="#" id="axesDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                          Travaux
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="axesDropdown">
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle">Axe 1</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/html_pages/travaux_GT1.html">GT1</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/html_pages/travaux_GT2.html">GT2</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe1/html_pages/travaux_GT3.html">GT3</a></li>
                                </ul>
                            </li>
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle">Axe 2</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/html_pages/travaux_GT4.html">GT4</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/html_pages/travaux_GT5.html">GT5</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe2/html_pages/travaux_GT6.html">GT6</a></li>
                                </ul>
                            </li>
                            <li class="dropdown-submenu">
                                <a class="dropdown-item dropdown-toggle">Axe 3</a>
                                <ul class="dropdown-menu">
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe3/html_pages/travaux_ethique.html">Enjeux éthiques</a></li>
                                    <li><a class="dropdown-item" href="https://consortiumariane.gitpages.huma-num.fr/axe3/html_pages/travaux_juridique.html">Questions juridiques</a></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-400 text-xl transition hover:text-gray-400/75" href="#">Actualités</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link text-gray-400 text-xl transition hover:text-gray-400/75" href="https://docs.google.com/forms/d/1nxWiaj88LY7R-poxxlTiUxdvyIH5hL5eBHFjgsfsKGg/viewform?edit_requested=true">Nous rejoindre</a>
                    </li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Contenu -->
    <div class="container-fluid">
        <div class="row">
            <main class="col-md-9 content">
                <div class="container-fluid">
                    <div class="container">
                        <div class="title-container">
                            <h1>Les travaux du GT{gt_number}</h1>
                            <hr>
                        </div>
                        <div class="row">
                            {documents_list}
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-light py-3">
        <div class="container d-flex justify-content-between align-items-center">
          <div class="text-center flex-grow-1 me-5">
            <p class="mb-0">&copy; 2024 Consortium HN Ariane. Tous droits réservés.</p>
          </div>
          <div class="ms-5">
            <a href="https://consortiumariane.gitpages.huma-num.fr/axe1/credits.html" class="mx-2">Crédits</a>
          </div>
          <div class="ms-5">
            <a href="https://consortiumariane.gitpages.huma-num.fr/axe1/mentions_legales.html" class="mx-2">Mentions légales</a>
          </div>
          <div class="ms-5">
            <a href="https://hal.science/CONSORTIUM-HN-ARIANE" target="_blank" rel="noopener noreferrer">
              <img src="assets/img/HAL_logotype-rvb_fond-clair_fr.png" class="img-fluid">
            </a>
          </div>
        </div>
      </footer>
</body>
</html>
"""

def create_html_page(title, gt_number, files, output_path):
    """ Génère une page HTML pour un groupe de travail donné. """
    if not title or not gt_number:
        print(f"Erreur : title ou gt_number est invalide. title={title}, gt_number={gt_number}")
        return

    # Regrouper les documents par année
    documents_by_year = {}
    for file in files:
        if isinstance(file, dict) and "date" in file:
            year = datetime.strptime(file["date"], "%Y-%m-%d").year
            if year not in documents_by_year:
                documents_by_year[year] = []
            documents_by_year[year].append(file)

    # Générer les sections HTML pour chaque année
    document_items = []
    for year, docs in sorted(documents_by_year.items(), reverse=True):
        year_items = "\n".join(
            f"""
            <div class="col-md-4 mb-4 d-flex">
                <div class="card w-100">
                    <a href="../{file.get('path', '#')}" target="_blank" style="text-decoration: none; color: inherit;">
                        <div class="card-body">
                            <h2 class="card-title">{file.get('title', 'Document inconnu')}</h2>
                        </div>
                    </a>
                </div>
            </div>
            """ for file in docs
        )
        document_items.append(f"<div class='row'><h2>{year}</h2><hr>{year_items}</div>")

    if not document_items:
        print("Aucun document à afficher.")
        document_items = "<p>Aucun document disponible.</p>"
    else:
        document_items = "\n".join(document_items)

    try:
        html_content = HTML_TEMPLATE.format(title=title, gt_number=gt_number, documents_list=document_items)
    except KeyError as e:
        print(f"Erreur : Placeholder manquant dans HTML_TEMPLATE : {e}")
        return

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"Page HTML générée : {output_path}")
    except IOError as e:
        print(f"Erreur lors de l'écriture du fichier {output_path}: {e}")

def load_documents(input_json):
    """ Charge les documents à partir du fichier JSON. """
    if not os.path.exists(input_json):
        print("Le fichier JSON n'existe pas. Exécute d'abord generate_json.py.")
        return None

    try:
        with open(input_json, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Erreur lors de la lecture du fichier JSON: {e}")
        return None

def categorize_documents(documents):
    """ Catégorise les documents par groupe de travail. """
    categories = {}
    for doc in documents:
        if "name" not in doc or "path" not in doc:
            print(f"Document invalide: {doc}")
            continue

        # Extraction du nom du document après GT*_DATE_
        parts = doc["name"].split("_")
        if len(parts) < 3:
            continue
        gt_prefix = parts[0]
        date_part = parts[1]
        doc_title = "_".join(parts[2:]).replace("_", " ")

        # Ajout du titre au document
        doc["title"] = doc_title

        # Ajout de la date au document si elle n'existe pas
        if "date" not in doc:
            try:
                doc["date"] = datetime.strptime(date_part, "%Y-%m-%d").strftime("%Y-%m-%d")
            except ValueError:
                doc["date"] = "2025-01-01"  # Date par défaut si le format est invalide

        if gt_prefix not in categories:
            categories[gt_prefix] = []
        categories[gt_prefix].append(doc)

    # Tri des documents : d'abord par date (descendant), puis par titre alphabétique
    for gt_prefix in categories:
        categories[gt_prefix].sort(key=lambda x: (datetime.strptime(x["date"], "%Y-%m-%d") if "date" in x else datetime.min, x["title"]), reverse=True)

    return categories

def generate_html_pages(input_json, output_dir):
    """ Parse le JSON et génère des pages HTML par groupe de travail. """
    documents = load_documents(input_json)
    if documents is None:
        return

    categories = categorize_documents(documents)

    os.makedirs(output_dir, exist_ok=True)

    for gt, files in categories.items():
        gt_number = gt.replace("GT", "")  # Extraction du numéro
        output_path = os.path.join(output_dir, f"travaux_{gt}.html")
        create_html_page(f"Travaux du {gt}", gt_number, files, output_path)

if __name__ == "__main__":
    generate_html_pages(INPUT_JSON, OUTPUT_DIR)
