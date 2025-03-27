import { z } from "zod";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "../../ui/card";
import { courseSchema } from "../../schemas/coursesSchema";
import { buttonVariants } from "../../ui/button";

type Course = z.infer<typeof courseSchema>;

interface CourseCardProps {
  course: Course;
}

function CourseCard({ course }: CourseCardProps) {
  return (
    <Card className="w-[24rem]">
      <CardHeader>
        <CardTitle>{course.name}</CardTitle>
        <CardDescription>{course.description}</CardDescription>
      </CardHeader>
      <CardContent className="flex flex-col gap-4">
        {course.teacher && <p>{course.teacher}</p>}
        {course.groups?.length ? (
          <ul>
            {course.groups.map((group) => (
              <li>{group}</li>
            ))}
          </ul>
        ) : (
          <p>Жодної групи.</p>
        )}
      </CardContent>

      <CardFooter>
        <a
          href={`courses/${course.id}`}
          className={buttonVariants({ variant: "outline" })}
        >
          Більше
        </a>
      </CardFooter>
    </Card>
  );
}

export default CourseCard;
