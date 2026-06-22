import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Task {
    private final String        id;
    private final LocalDateTime createdAt;

    private String              desc;
    private Status              status;
    private LocalDateTime       updatedAt;

    enum Status {
        TODO, IN_PROGRESS, DONE;
    }

    public Task(String id, String desc, LocalDateTime createdAt) {
        this.id     = id;
        this.desc   = desc;
        this.status = Status.TODO;

        this.createdAt = createdAt;
        this.updatedAt = createdAt;
    }

    public void updateDesc(String newDesc)      { this.desc = newDesc; }
    public void updateTime(LocalDateTime time)  { this.updatedAt = time; }
    public void updateStatus(byte newStatus) {
        switch (newStatus) {
            case 0:
                this.status = Status.TODO;
                break;
            case 1:
                this.status = Status.IN_PROGRESS;
                break;
            case 2:
                this.status = Status.DONE;
                break;
            default:
                throw new IllegalArgumentException("Invalid status. Only 0, 1, and 2 are allowed.");
        }
    }

    public String getId()       { return this.id;   }
    public String getDesc()     { return this.desc; }
    public String getStatus()   { return this.status.toString(); }

    public String getCreatedAt() { return dateToStr(this.createdAt); }
    public String getUpdatedAt() { return dateToStr(this.updatedAt); }

    private String dateToStr(LocalDateTime time) {
        DateTimeFormatter fmt = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm");
        
        return time.format(fmt);
    }
}