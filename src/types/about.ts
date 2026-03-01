export interface BioData {
 name: string;
 title: string;
 profileImage: string;
 biography: string;
 email: string;
 location: string;
 socialLinks: {
   linkedin?: string;
   github?: string;
   twitter?: string;
 };
}

export interface SkillsCategory {
 category: string;
 skills: { name: string; level: number }[];
}

export interface WorkExperience {
 id: string;
 company: string;
 role: string;
 startDate: string;
 endDate: string | null;
 description: string;
 location: string;
 highlights: string[];
}

export interface Education {
 id: string;
 institution: string;
 degree: string;
 field: string;
 startDate: string;
 endDate: string;
 gpa?: string;
 achievements?: string[];
}
