walker summarize_paragraph{
    has paragraph;
    can cl_summer.summarize;

    summary = cl_summer.summarize(text = paragraph, sent_count = 2, summarizer_type = "LsaSummarizer");

    report summary;
}

walker generate_image {

    has text;
    can text-to-image.generate;

    image = text-to-image.generate (text = text);

    report image;
}