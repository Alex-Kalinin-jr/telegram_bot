--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3 (Debian 16.3-1.pgdg120+1)
-- Dumped by pg_dump version 16.3 (Debian 16.3-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying NOT NULL,
    description character varying
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.categories_id_seq OWNER TO postgres;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: links; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.links (
    id integer NOT NULL,
    position_id integer,
    img character varying
);


ALTER TABLE public.links OWNER TO postgres;

--
-- Name: links_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.links_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.links_id_seq OWNER TO postgres;

--
-- Name: links_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.links_id_seq OWNED BY public.links.id;


--
-- Name: positions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.positions (
    id integer NOT NULL,
    "position" character varying NOT NULL,
    category_id integer,
    description character varying
);


ALTER TABLE public.positions OWNER TO postgres;

--
-- Name: positions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.positions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.positions_id_seq OWNER TO postgres;

--
-- Name: positions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.positions_id_seq OWNED BY public.positions.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: links id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.links ALTER COLUMN id SET DEFAULT nextval('public.links_id_seq'::regclass);


--
-- Name: positions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions ALTER COLUMN id SET DEFAULT nextval('public.positions_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
e9324901031a
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categories (id, name, description) FROM stdin;
1	мебельные щиты	Высококачественный и универсальный материал для изготовления мебели, столешниц, подоконников, подлокотников и других изделий. Мы предлагаем два типа мебельных щитов: сращенные и цельноламельные. Сращенные щиты состоят из небольших ламелей, склеенных между собой, что обеспечивает им высокую прочность и стабильность формы. Цельноламельные щиты, в свою очередь, изготавливаются из цельных кусков древесины, что придает им уникальный природный рисунок и текстуру. Наши мебельные щиты отличаются точностью размеров, гладкой поверхностью и простотой в обработке. Мы предлагаем индивидуальный подход и поможем подобрать подходящий материал, учитывая ваши потребности и задачи. 🪑🌳🤝
2	готовые изделия	Наша категория готовых изделий включает качественные столешницы, ступени и подоконники, изготовленные из лучших мебельных щитов. Мы предлагаем широкий ассортимент продукции, соответствующей самым высоким стандартам качества и дизайна. 🪑🌳🤝
3	напольные покрытия	Напольные покрытия из дерева - это экологичность, эстетичный внешний вид, при правильном уходе и эксплуатации их срок службы неорганичен. Мы предлагаем покрытия из лиственницы, отличающейся огромной влагостойкостью, защитой от гниения, высокой прочностью и твердостью. 
\.


--
-- Data for Name: links; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.links (id, position_id, img) FROM stdin;
2	2	table_1.jpeg
3	2	table_6.jpeg
5	4	slab_1.jpeg
6	4	table_3.jpeg
7	5	windowsail_5.jpeg
8	5	windowsail_7.jpeg
9	6	windowsill_2.jpeg
10	7	table_2.jpeg
11	7	table_11.jpeg
12	8	table_15.jpeg
13	8	table_9.jpeg
14	8	table_5.jpeg
15	9	stair_1.jpeg
16	9	stair_2.jpeg
17	9	stair_3.jpeg
18	11	floor_0.jpeg
19	11	floor_1.jpeg
20	11	floor_2.jpeg
21	10	parquet_2.jpeg
22	10	parquet_3.jpeg
23	10	parquet_4.jpeg
24	10	parquet_5.jpeg
25	10	parquet_6.jpeg
26	10	parquet_7.jpeg
1	1	oak.jpeg
27	1	oak_3.jpeg
28	1	oak_4.jpeg
29	3	birch_5.jpeg
30	3	birch_1.jpeg
31	3	birch_4.jpeg
32	3	birch_2.jpeg
33	3	birch_6.jpeg
\.


--
-- Data for Name: positions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.positions (id, "position", category_id, description) FROM stdin;
1	Щит из дуба	1	Мебельный щит из дуба 🌰 Элегантность и долговечность. Идеальный выбор для ценителей качества. Дубовые щиты отличаются прочностью, стойкостью к износу и влаге.\n 📞 Персонализированная обработка и финишное покрытие.
2	Щит из лиственницы	1	Лиственница выделяется своей устойчивостью к влаге и грибкам, к ударам и истиранию, а также обладает отличной звуко- и теплоизоляцией.\n 📞 Персонализированная обработка и финишное покрытие.
3	Щит из березы	1	🌳 Березовые щиты обладают высокой плотностью и прочностью,  это идеальный выбор для изготовления мебели, подверженной высоким нагрузкам. Благодаря светлому цвету и однородной текстуре, березовые щиты легко окрашиваются, позволяя создавать изделия различного дизайна и цвета.\n 📞 Персонализированная обработка и финишное покрытие.
4	Столешницы из слэбов	2	Столешницы из слэбов\n 🏠 Уникальное изготовление по вашему дизайну. Аутентичный вид натурального дерева украсит пространство.\n 📞 Персонализированная обработка и финишное покрытие.
5	Подоконники	2	Подоконники из мебельных щитов\n 🏠 Изготовлены на заказ для гармонии в интерьере. Натуральная древесина для элегантности помещения.\n 📞 Индивидуальное изготовление и покрытие ЛКМ.
6	Подлокотники	2	Подлокотники из мебельных щитов\n 🏠 Обеспечивают уют и гармонию вашего интерьера. Использование натуральной древесины подчеркивает каждый элемент.\n 📞 Предлагаем индивидуальное производство, обработку и покрытие ЛКМ.
7	Раковины из дерева	2	Раковины из мебельных щитов\n 🏠 \n Для ценителей необычного.\n 📞 Мы предлагаем изготовление, обработку и покрытие ЛКМ по индивидуальному проекту.
8	Столешницы	2	Столешницы из мебельных щитов\n 🏠 Прочные и функциональные, идеально подходят для кухни или офиса.\n Мебельные щиты гарантируют ровную поверхность и легкость в уходе. Выберите из множества пород дерева для создания уникального дизайна.\n 📞 Оформите заказ на изготовление, обработку и покрытие ЛКМ.
9	Ступени	2	Ступени лестниц из мебельных щитов\n 🏠 Идеальное сочетание надежности и стиля для вашего дома или офиса. Изготавливаются из качественной древесины для гарантии долговечности и безопасности.\n 📞 Заказывайте изготовление, обработку и покрытие ЛКМ по вашему вкусу.
10	Паркет из лиственницы	3	Паркет из массива лиственницы отличается резистентностью к ударным нагрузкам, твердостью, невосприимчивостью к влаге. При правильной эксплуатации срок службы неограничен. 📞 Персонализированная обработка и финишное покрытие.
11	Доска пола	3	Прочность, устойчивость к искажениям и деформациям, а также удобство в установке. Сращенная доска пола из лиственницы имеет гладкую поверхность и простую обработку, что делает ее идеальным выбором для создания эстетически привлекательных и функциональных половых покрытий.\\n  📞 Персонализированная обработка и финишное покрытие.
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_id_seq', 3, true);


--
-- Name: links_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.links_id_seq', 33, true);


--
-- Name: positions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.positions_id_seq', 11, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: links links_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.links
    ADD CONSTRAINT links_pkey PRIMARY KEY (id);


--
-- Name: positions positions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_pkey PRIMARY KEY (id);


--
-- Name: ix_links_position_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_links_position_id ON public.links USING btree (position_id);


--
-- Name: links links_position_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.links
    ADD CONSTRAINT links_position_id_fkey FOREIGN KEY (position_id) REFERENCES public.positions(id);


--
-- Name: positions positions_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.positions
    ADD CONSTRAINT positions_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.categories(id);


--
-- PostgreSQL database dump complete
--

