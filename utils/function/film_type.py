async def film_type_hashtag(film_type: str):
    type_strip = film_type.strip()
    type_template_fist_latter = type_strip[0]
    type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}",
                                                 f"#{type_template_fist_latter}")
    return type
