--
-- PostgreSQL database dump
--

\restrict qxEXUDN6ISq5b6TTTZwtNY87PoMUY9ulqQSFBm3tR0rXTFODajf17Qa6cfuWYl5

-- Dumped from database version 18.4
-- Dumped by pg_dump version 18.4

-- Started on 2026-07-11 11:27:53

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 220 (class 1259 OID 16394)
-- Name: Faculty ; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Faculty " (
);


ALTER TABLE public."Faculty " OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16397)
-- Name: faculty; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.faculty (
    faculty_id character varying(10) NOT NULL,
    name character varying(100),
    subject character varying(50),
    experience_years integer
);


ALTER TABLE public.faculty OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16447)
-- Name: leaderboard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.leaderboard (
    rank integer,
    student_id character varying(10),
    name character varying(100),
    batch character varying(20),
    average_score numeric(5,2)
);


ALTER TABLE public.leaderboard OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16434)
-- Name: results; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.results (
    result_id integer NOT NULL,
    student_id character varying(10),
    test_id character varying(10),
    physics integer,
    chemistry integer,
    maths integer,
    total integer,
    rank integer
);


ALTER TABLE public.results OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16433)
-- Name: results_result_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.results_result_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.results_result_id_seq OWNER TO postgres;

--
-- TOC entry 5043 (class 0 OID 0)
-- Dependencies: 223
-- Name: results_result_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.results_result_id_seq OWNED BY public.results.result_id;


--
-- TOC entry 219 (class 1259 OID 16388)
-- Name: students; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.students (
    student_id character varying(10) NOT NULL,
    name character varying(100),
    phone character varying(20),
    email character varying(100),
    batch character varying(20),
    joining_date date,
    fees integer,
    paid integer,
    remaining integer,
    attendance integer
);


ALTER TABLE public.students OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 16441)
-- Name: study_material; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.study_material (
    material_id character varying(10) NOT NULL,
    subject character varying(50),
    chapter character varying(100),
    pdf_name character varying(255)
);


ALTER TABLE public.study_material OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16427)
-- Name: tests; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tests (
    test_id character varying(10) NOT NULL,
    test_name character varying(100),
    subject character varying(50),
    max_marks integer,
    test_date date
);


ALTER TABLE public.tests OWNER TO postgres;

--
-- TOC entry 4880 (class 2604 OID 16437)
-- Name: results result_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results ALTER COLUMN result_id SET DEFAULT nextval('public.results_result_id_seq'::regclass);


--
-- TOC entry 4884 (class 2606 OID 16402)
-- Name: faculty faculty_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.faculty
    ADD CONSTRAINT faculty_pkey PRIMARY KEY (faculty_id);


--
-- TOC entry 4888 (class 2606 OID 16440)
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.results
    ADD CONSTRAINT results_pkey PRIMARY KEY (result_id);


--
-- TOC entry 4882 (class 2606 OID 16393)
-- Name: students students_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.students
    ADD CONSTRAINT students_pkey PRIMARY KEY (student_id);


--
-- TOC entry 4890 (class 2606 OID 16446)
-- Name: study_material study_material_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.study_material
    ADD CONSTRAINT study_material_pkey PRIMARY KEY (material_id);


--
-- TOC entry 4886 (class 2606 OID 16432)
-- Name: tests tests_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tests
    ADD CONSTRAINT tests_pkey PRIMARY KEY (test_id);


-- Completed on 2026-07-11 11:27:53

--
-- PostgreSQL database dump complete
--

\unrestrict qxEXUDN6ISq5b6TTTZwtNY87PoMUY9ulqQSFBm3tR0rXTFODajf17Qa6cfuWYl5

